import java.util.concurrent.ThreadLocalRandom;
import java.util.ArrayList;
import java.util.List;
public class BlackJackTaules {
	
//	CONSTANTS
	public static int [] valor = {1,2,3,4,5,6,7,8,9,10,10,10,10};
	public static int [] barallaRobar = {4,4,4,4,4,4,4,4,4,4,4,4,4};
	
//	DADES GENERALS
	public static int resetCartes = 0;
	public static int contadorBasic = 0;
	public static int partides = 1000000;
	public static int guanyades = 0;
	public static int perdudes = 0;
	public static int empats = 0;
	
//	DADES PER PARTIDA
	public static int cartesRestants = 52;
	
//	DADES PER TORN (JUGADOR O BANCA)
	public static List<Integer> cartesTorn = new ArrayList<Integer>();
	public static boolean asTrobat;
	public static int valorBrut;
	public static int valorBanca;
	public static int valorJugador;
//	valorBrut és el valor de la banca o jugador considerant que l'As té valor 1.
//	valorBanca és el valor de la banca considerant la millor ponderació d'As que no fa superar 21.
//	valorJugador és el valor del jugador considerant la millor ponderació d'As que no fa superar 21.
	
	public static void main(String[] args) {
		jugarPartides();
		printResultats();
	}
		
	public static void jugarPartides() {
		for (int p=0; p<partides; ++p)
		{
			cartesTorn.clear();
//			System.out.println("Partida " + (p+1) + ":");
//			TORN DEL JUGADOR
			resetJugador();
			tornJugador();
			if (valorJugador > 21)
			{
				++ perdudes;
//				System.out.println();
//				System.out.println("____________________");
				continue;
			}
//			System.out.println();
//			TORN DE LA BANCA
			resetBanca();
			tornBanca();
			if (valorBanca > 21)
			{
				++ guanyades;
//				System.out.println();
//				System.out.println("____________________");
				continue;
			}
			compararResultats();
//			System.out.println();
//			System.out.println("____________________");
		}
	}
	
	public static void tornJugador() {
		while (JugadorRoba())
		{
			int carta = robar();
//			System.out.print(valor[carta] + ", ");
			if (carta == 0) asTrobat = true;
			valorBrut = valorBrut + valor[carta];
		}
		valorJugador = rentar(valorBrut);
	}
	
	public static void tornBanca() {
		while(BancaRoba())
		{
			int carta = robar();
//			System.out.print(valor[carta] + ", ");
			if (carta == 0) asTrobat = true;
			valorBrut = valorBrut + valor[carta];
		}
		valorBanca = rentar(valorBrut);
	}
	
	public static void resetJugador() {
		asTrobat = false;
		valorBrut = 0;
		valorJugador = 0;
	}
	
	public static void resetBanca() {
		asTrobat = false;
		valorBrut = 0;
		valorBanca = 0;
	}
	
	public static void compararResultats() {
		if (valorBanca > valorJugador) ++ perdudes;
		else if (valorBanca < valorJugador) ++ guanyades;
		else ++ empats;
	}
	
	public static void printResultats() {
		System.out.println("Guanyades: " + guanyades);
		System.out.println("Perdudes: " + perdudes);
		System.out.println("Empats: " + empats);
	}
	
	public static int rentar(int valorBrut) {
		if (asTrobat && (valorBrut + 10 <= 21)) return valorBrut + 10;
		else return valorBrut;
	}
	
	public static boolean JugadorRoba() {
		
//		TÈCNICA 2 - Conteix Hi-Lo
//		Aquesta tècnica fa servir un conteig molt elemental:
//		https://es.blackjack.org/blackjack-estrategia/conteo-de-cartas/
//		El conteig comença en (0) quan hi ha una nova "barajada"
//		Les cartes 2,3,4,5,6 sumen 1.
//		Les cartes 7,8,9 sumen 0.
//		Les cartes 1,10,J,Q,K resten 1.
//		Com més alta sigui la suma, més fàcil és que hi hagi cartes altes.
//		Com més baixa sigui la suma, més fàcil és que hi hagi cartes baixes.
		
		if (asTrobat == true)
		{
			if(valorBrut + 10 < 17) return true;
			else if (valorBrut + 10 <= 21) return false;
			else if (valorBrut >= 17) return false;
			else return true;
		}
		else if (valorBrut < 15) return true;
		return false;
	}
	
//	TÈCNICA 3 - Uston SS
//	Aquesta tècnica fa servir un conteig més especialitzat (Uston SS):
//	https://es.blackjack.org/blackjack-estrategia/conteo-de-cartas/
//	Ara, a diferència d'abans, hi ha diferents ponderacions per cada carta:
//	Les cartes 2,4,6 sumen 2.
//	La carta 5 suma 3.
//	La carta 7 suma 1.
//	La carta 8 suma 0.
//	La carta 9 resta 1.
//	Les cartes 1,10,J,Q,K resten 2.
//	Les cartes 7,8,9 no alteren la suma.
//	Les cartes 1,10,J,Q,K resten 1.
//	Com més alta sigui la suma, més fàcil és que hi hagi cartes altes.
//	Com més baixa sigui la suma, més fàcil és que hi hagi cartes baixes.
	
	public static boolean BancaRoba() {
		if (asTrobat == true)
		{
			if(valorBrut + 10 < 17) return true;
			else if (valorBrut + 10 <= 21) return false;
			else if (valorBrut >= 17) return false;
			else return true;
		}
		else if (valorBrut < 17) return true;
		return false;
	}
	
	public static int robar() {
		if (cartesRestants == 0)
		{
//			Aquí haurem de fer un reset de les cartes:
//			(Retornar a la baralla de robar totes les cartes que han sortit i no estan a les mans)
			for (int i=0; i<13; ++i) barallaRobar[i] = 4;
			for (int i=0; i<cartesTorn.size(); ++i) -- barallaRobar[cartesTorn.get(i)];
			cartesRestants = 52-cartesTorn.size();
			++ resetCartes;
		}
//		Anem a treure una carta completament aleatòria entre les que queden:
		int c = ThreadLocalRandom.current().nextInt(1, cartesRestants + 1);
		for (int i=0; i<13; ++i)
		{
			c = c - barallaRobar[i];
			if (c <= 0)
			{
				-- barallaRobar[i];
				-- cartesRestants;
				cartesTorn.add(i);
				if (i==0 || i>=9) -- contadorBasic;
				else if (i<6) ++ contadorBasic;
				return i;
			}
		}
		return 0;
	}

}
