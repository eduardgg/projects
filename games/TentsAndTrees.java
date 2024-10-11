import java.util.ArrayList;
import java.util.List;
import javafx.util.Pair;

public class TentsAndTrees {
	
//  _______________________________________________________________________________________________________
	
//	DADES PEL JOC:
	
//	DADES JOC 1: (Tamany 8)
//	public static String dificultat = "Difícil";
//	public static int n = 8;
//	public static int [] tpc = {3,1,3,1,2,1,1,2};
//	public static int [] tpf = {2,2,2,0,3,1,1,3};
//	public static int [][] posicioArbres = 
//			{{1},{0,2,6},{4},{2,3},{1,4},{7},{0,2},{3,6}};
			
//	DADES JOC 2: (Tamany 16)
//	public static String dificultat = "Difícil";
//	public static int n = 16;
//	public static int [] tpc = {5,2,5,0,4,2,3,3,3,2,3,4,2,4,2,4};
//	public static int [] tpf = {5,2,3,3,2,5,1,6,1,3,4,1,2,4,2,4};
//	public static int [][] posicioArbres = 
//			{{1,9,11,13},{2,5},{8},{0,3,4,7,14},{4,10,13},{6,11,14},{0,2,11},{1,4},
//			 {0,6,7,13,15},{0,13,14},{1,5,8,10},{4,7},{},{0,6,8,12},{3,7,11,15},{5,10,12}};
	
//	DADES JOC 3: (Tamany 18)
	public static String dificultat = "Difícil";
	public static int n = 18;
	public static int [] tpc = {5,3,3,2,3,4,2,5,2,3,6,2,4,2,6,1,5,3};
	public static int [] tpf = {4,4,2,5,3,4,2,3,3,4,4,2,2,5,1,5,2,6};
	public static int [][] posicioArbres =
			{{8,12,13},{1,3,9,17},{4,6,14},{7,10,13,14},{0,1,2,7,11,16,17},{4},{5,9,13,17},{11},{1,6,9},
			{2,11},{4,5,14,17},{0,4,7,11},{1,15,16},{9,12},{4,7,8,14,16},{10},{0,4,6,7,11},{2,9,13,15,16}};
			 
//  _______________________________________________________________________________________________________

// INFORMACIÓ MAIN:
//	La funció gespaAïllada només té sentit fer-la a l'inici, una vegada.
//	La idea final seria fer un bucle que repeteixi les altres tècniques fins acabar el joc.
//	Les podem anar repetint una i una altra vegada, i anar-les alternant entre elles.
//	El bucle acabaria quan el bool jocAcabat és true (quan ja no queden caselles desconegudes).			
			
//	NOTACIÓ:
//	0 = Desconegut
//	1 = Tree
//	2 = Gespa
//	3 = Tent
	
//	COORDENADES:
//	- Primera coordenada (0: n-1): Número de la fila
//	- Segona coordenada (0: n-1): Número de la columna
	
//	VARIABLES:
//	camp: matriu quadrada n x n d'objectes (dades i també solució)
//	tpc: vector de tamany n de tendes per columna (cada índex identifica la columna)
//	tpf: vector de tamany n de tendes per fila (cada índex identifica la fila)
//	trpc: vector de tamany n de tendes restants per identificar per columna (cada índex identifica la columna)
//	trpf: vector de tamany n de tendes restants per identificar per fila (cada índex identifica la fila)
	
//	ENTRADES I SORTIDES:
//	L'entrada és el valor de n, les posicions on hi ha tree i el nombre de tendes per fila i columna
//	Això és el valor de n, les posicions dels 1s en la matriu camp i els vectors tpf i tpc
//	La sortida és simplement la matriu camp plena amb els valors de gespa, trees i tents
	
//	TÈCNIQUES BÀSIQUES:
//	- 1. Completem totes les files o columnes que ja no els falta cap tenda
//	- 2. Omplim de gespa les caselles que no tenen cap arbre contigu
//	- 3. Quan col·loquem una tenda, omplim de gespa els espais desconeguts del voltant (8 caselles al voltant)
	
//	TÈCNIQUES AVANÇADES:
//	- Chetar files / columnes. La comentem més endavant
//	- Aparellaments de tendes i arbres i identificació de parelles
//	- Gespa aïllada millorada (considera les parelles anteriors)
	
//	MANCANCES:
//	- Només funciona per matrius de camp quadrades. Seria bo millorar-lo per a camps rectangulars.
	
//	IMPORTANT!!!:
//	Cada cop que trobem una tenda en una casella (i,j), hem de fer les següents modificacions:
//	1. Restar una unitat a trpf(i) i a trpc(j)
//	2. Afegir una unitat al contador tendesLocalitzades
//	3. Aplicar la funció envoltar (i,j,n,camp)
			
//	ALGUNES CONCLUSIONS:
//	1. Per resoldre el joc 1 només ha calgut gespa aïllada un cop, i un bucle de chetar files i columnes
//	2. Per resoldre el joc 2 no n'hi ha hagut prou amb això, i hem hagut d'implementar la funció d'aparellaments
//	3. Per resoldre el joc 3 no n'hi ha hagut prou amb les anteriors funcions, i hem millorat la funció "gespaAïllada" per poder-la
//	posar dins el bucle i consideri també les parelles fetes. El que ha estat definitiu és la nova funció "identificarParelles",
//	ja que al chetar files i columnes es posaven tendes però no es deia quina era la seva parella, una dada crucial per la funció
//	gespaAïllada millorada

//  _______________________________________________________________________________________________________

//	VARIABLES DEL CODI:
//	Faig una còpia, ja que sinó Java em modificaria els dos objectes cada cop que un canvia.
//	És un problema que encara no he sabut resoldre.
	public static int [] trpc = copy(tpc);
	public static int [] trpf = copy(tpf);
	public static boolean [] filaAcabada = falsos(n);
	public static boolean [] columnaAcabada = falsos(n);
	public static int tendesTrobades = 0;
	public static int [][] camp = colocarArbres(posicioArbres);
	public static int [][] parelles = matriuInicialitzada(n,-1);
	public static int [][] campBuit = copy(camp);
	public static int nombreParelles = 10;
	public static int nombreArbres = quants(posicioArbres);
	public static int nombreIteracions = 0;
	public static int iteracionsMax = 10;
	
	public static void main(String[] args) {
		while (tendesTrobades != nombreArbres)
		{
//			System.out.println("Iteració: " + (iteracions + 1));
			gespaAïllada(camp);
			for (int i=0; i<n; ++i) chetarFila(i, trpf, trpc, camp);
			for (int j=0; j<n; ++j) chetarColumna(j, trpf, trpc, camp);
			identificarParelles();
			while (true)
			{
				int num = tendesTrobades;
				aparellaments();
				if (tendesTrobades == num) break;
			}
			++ nombreIteracions;
			if (nombreIteracions == iteracionsMax) break;
		}
		printSolucio();
	}
	
	public static int quants(int [][] posicions)
	{
		int quantitat = 0;
		for (int i=0; i<posicions.length; ++i) quantitat += posicions[i].length;
		return quantitat;
	}
	
	public static void printMat(int [][] matriu) {
		for (int i=0; i<matriu.length; ++i)
		{
			for (int j=0; j<matriu[i].length; ++j)
			{
				System.out.print(matriu[i][j] + " ");
			}
			System.out.println();
		}
		System.out.println();
	}
	
	public static int [][] matriuInicialitzada (int n, int val) {
		int [][] mat = new int [n][n];
		for (int i=0; i<n; ++i) for (int j=0; j<n; ++j) mat [i][j] = val;
		return mat;
	}
	
	public static void printSolucio () {
		System.out.println();
		System.out.println("Tents & Trees");
		System.out.println("Tamany del tauler: " + n + "x" + n);
		System.out.println("Dificultat: " + dificultat);
//		Podem imprimir també la "plantilla" del joc:
		System.out.println();
		printJoc(campBuit, tpf, tpc);
		System.out.println();
		System.out.println("SOLUCIÓ:");
		System.out.println();
		printJoc(camp, tpf, tpc);
		System.out.println("Tendes Trobades: " + tendesTrobades + "/" + nombreArbres);
		System.out.println("Nombre de parelles fetes: " + (nombreParelles-10));
		System.out.println("Nombre d'iteracions: " + nombreIteracions);
	}
	
	public static int [][] colocarArbres (int[][] posicions) {
		int [][] mat = matriuInicialitzada(n,0);
		for (int i=0; i<posicions.length; ++i)
		{
			for (int j=0; j<posicions[i].length; ++j)
			{
				mat [i][posicions[i][j]] = 1;
			}
		}
		return mat;
	}
	
	public static boolean [] falsos (int n) {
		boolean [] falsos = new boolean [n];
		for (int i=0; i<n; ++i) falsos[i] = false;
		return falsos;
	}
	
	public static boolean jocAcabat(int [][] m) {
		for (int i=0; i<m.length; ++i)
		{
			for (int j=0; j<m[0].length; ++j)
			{
				if (m[i][j] == 0) return false;
			}
		}
		return true;
	}
	
	public static void actualitzarFilaAcabada(int i) {
		for (int j=0; j<n; ++j) if (camp[i][j] == 0) return;
		filaAcabada[i] = true;
	}
	
	public static void actualitzarColumnaAcabada(int j) {
		for (int i=0; i<n; ++i) if (camp[i][j] == 0) return;
		columnaAcabada[j] = true;
	}
	
	public static int[] copy(int [] v)  {
		int [] copy = new int [v.length];
		for (int i=0; i<v.length; ++i) copy[i] = v[i];
		return copy;
	}
	
	public static int[][] copy(int [][] m) {
		int [][] copy = new int [m.length][m[0].length];
		for (int i=0; i<m.length; ++i)
			for (int j=0; j<m[0].length; ++j)
				copy[i][j] = m[i][j];
		return copy;
	}
	
	public static double[][] transpose(double [][] m) {
        double[][] temp = new double[m[0].length][m.length];
        for (int i = 0; i < m.length; i++)
            for (int j = 0; j < m[0].length; j++)
                temp[j][i] = m[i][j];
        return temp;
    }
	
	public static int[][] transpose(int [][] m) {
        int [][] temp = new int [m[0].length][m.length];
        for (int i = 0; i < m.length; i++)
            for (int j = 0; j < m[0].length; j++)
                temp[j][i] = m[i][j];
        return temp;
    }
	
	public static int[] columna(int j, int [][] m) {
		int [] columna = new int [m.length];
		for (int i=0; i<m.length; ++i) columna[i] = m[i][j];
		return columna;
	}
	
	public static void printJoc (int [][] camp, int [] tpf, int [] tpc) {
		System.out.print("  | ");
		for (int i=0; i<n; ++i) System.out.print(tpc[i] + " ");
		System.out.println();
		System.out.print("__|_");
		for (int i=0; i<n; ++i) System.out.print("__");
		System.out.println();
		for (int i=0; i<n; ++i)
		{
			System.out.print(tpf[i] + " | ");
			for (int j=0; j<n; ++j) System.out.print(simbol(camp[i][j]) + " ");	
			System.out.println();
		}
		System.out.println();
	}
	
	public static char simbol(int num) {
		if (num == 1) return 'T';
		if (num == 2) return '-';
		if (num == 3) return 'X';
		else return ' ';
	}
	
	public static void omplir(int [][] camp, int i, int j, int codi) {
//		Aquesta funció només omple les caselles que compleixen les condicions:
//		1. Són caselles vàlides (dins la quadrícula del camp)
//		2. Estan en estat desconegut (ni tenda, ni arbre, ni gespa)
		if (i<0 || i>=n || j<0 || j>=n) return;
		if (camp[i][j] == 0) camp[i][j] = codi;
	}
	
	public static void omplir(int [] vec, int i, int codi) {
//		Aquesta funció només omple les caselles que compleixen les condicions:
//		1. Són caselles vàlides (dins la quadrícula del camp=
//		2. Estan en estat desconegut (ni tenda, ni arbre, ni gespa)
		int n = vec.length;
		if (i<0 || i>=n) return;
		if (vec[i] == 0) vec[i] = codi;
	}
	
	public static void gespaAïllada(int [][] camp) {
//		Omplim de gespa les caselles que no tenen cap arbre contigu
//		Aixo només cal fer-se una vegada, al principi, i és independent de la tècnica 1 (arribem al mateix)
		for (int i=0; i<n; ++i)
		{
			for (int j=0; j<n; ++j)
			{
				boolean esquerra = (j == 0 || camp [i][j-1] == 0 || camp [i][j-1] == 2 || parelles[i][j-1] != -1);
				boolean dreta = (j == n-1 || camp [i][j+1] == 0 || camp [i][j+1] == 2 || parelles[i][j+1] != -1);
				boolean sobre = (i == 0 || camp [i-1][j] == 0 || camp [i-1][j] == 2 || parelles[i-1][j] != -1);
				boolean sota = (i == n-1 || camp [i+1][j] == 0 || camp [i+1][j] == 2 || parelles[i+1][j] != -1);
				boolean centre = (camp [i][j] == 0);
				boolean aïllat = esquerra && dreta && sobre && sota && centre;
				if (aïllat) omplir(camp,i,j,2);
			}
		}
	}
	
	public static void gespaCaca(int [][] camp) {
//		Omplim de gespa les caselles que no tenen cap arbre contigu
//		Aixo només cal fer-se una vegada, al principi, i és independent de la tècnica 1 (arribem al mateix)
		for (int i=0; i<n; ++i)
		{
			for (int j=0; j<n; ++j)
			{
				boolean esquerra = (j == 0 || camp [i][j-1] != 1);
				boolean dreta = (j == n-1 || camp [i][j+1] != 1);
				boolean sobre = (i == 0 || camp [i-1][j] != 1);
				boolean sota = (i == n-1 || camp [i+1][j] != 1);
				boolean centre = (camp [i][j] != 1);
				boolean aïllat = esquerra && dreta && sobre && sota && centre;
				if (aïllat) camp [i][j] = 2; 
			}
		}
	}
	
	public static void envoltar(int [][] camp, int i, int j) {
//		Omplim de gespa els espais desconeguts del voltant de les tendes (8 caselles al voltant)
//		Aplicarem aquest mètode a la casella (i,j) d'una tenda, sempre que sigui col·locada
		omplir(camp, i-1, j-1, 2);
		omplir(camp, i-1, j, 2);
		omplir(camp, i-1, j+1, 2);
		omplir(camp, i, j-1, 2);
		omplir(camp, i, j+1, 2);
		omplir(camp, i+1, j-1, 2);
		omplir(camp, i+1, j, 2);
		omplir(camp, i+1, j+1, 2);
	}
	
	public static int capacitat(int [] vec) {
		int l = vec.length;
		int capacitat = 0;
		int espaiForat = 0;
		for (int j=0; j<l; ++j)
		{
			if (vec[j] == 0) ++espaiForat;
			else
			{
				capacitat += (int) ((espaiForat+1)/2);
				espaiForat = 0;
			}
		}
		capacitat += (int) ((espaiForat+1)/2);
		return capacitat;
	}
	
	public static void chetarFila(int i, int [] trpf, int [] trpc, int [][] camp) {
		
//		La idea de chetar (fila o columna) és la següent:
//		Definim un forat com un conjunt de caselles seguides amb valor desconegut totes elles.
//		Definim la capacitat d'un forat com el nombre de tendes que hi caben.
//		Si el forat té tamany f, està clar que la seva capacitat és floor((f+1)/2).
//		Comptem el nombre de forats que hi ha en aquella fila o columna i les seves capacitats
//		Trobem la capacitat total com a suma de capacitats parcials.
//		Comparem la capacitat total amb les tendes restants en aquella fila o columna.
//		La tècnica ens és útil quan la diferència entre capacitat total i tendes restants a col·locar val 0 o 1.
//		En aquest cas es poden fer algunes deduccions. Si és major que 1 no en podem fer cap.
		
//		CAS diferencia = 0:
//		Es procedeix a posar gespa i tendes seguint un codi bastant senzill.
		
//		CAS diferencia = 1:
//		Ara el que farem és suposar que en la fila superior o inferior s'ha col·locat una tenda, en una posició j (i ho farem per cada j).
//		En cas que la nova capacitat sigui < trpf, voldrà dir que hem arribat a una contradicció (NO tenim prou espai per tantes tendes!).
//		Per tant, haurà d'haver-hi gespa a sobre i sota de la posició (i,j). És a dir (i-1,j) i (i+1,j).
		
//		CAS diferencia > 1:
//		Crec que aquí no es pot fer res. No programarem cap mètode.
		
		if (filaAcabada [i]) return;
		
//		Primer completem la fila si ja no li falta cap tenda:
		if (trpf [i] == 0)
		{
			for (int j=0; j<n; ++j) omplir(camp, i, j, 2);
			return;
		}
		
		int capacitat = capacitat(camp[i]);
		int diferencia = capacitat - trpf[i];
		if (diferencia == 0)
		{
			int espaiForat = 0;
			for (int j=0; j<=n; ++j)
			{
				if (j<n && camp[i][j] == 0) ++espaiForat;
				else
				{
					if (espaiForat%2 == 1)
					{
						for (int k=0; k<(int) ((espaiForat+1)/2); ++k)
						{
							int pos = j-espaiForat+2*k;
							omplir(camp,i,pos,3);
							envoltar(camp,i,pos);
							++ tendesTrobades;
							-- trpf[i];
							-- trpc[pos];
						}
					}
					else
					{
						for (int k=0; k<espaiForat/2; ++k)
						{
							int pos = j-espaiForat+2*k;
							omplir(camp,i-1,pos,2);
							omplir(camp,i+1,pos,2);
							omplir(camp,i-1,pos+1,2);
							omplir(camp,i+1,pos+1,2);
						}
					}
					espaiForat = 0;
				}
			}
		}
		if (diferencia == 1)
		{
			for (int j=0; j<n; ++j)
			{
				int [] vec = copy(camp[i]);
				omplir(vec, j-1, 2);
				omplir(vec, j, 2);
				omplir(vec, j+1, 2);
				if (capacitat(vec) < trpf[i])
				{
					omplir(camp,i-1,j,2);
					omplir(camp,i+1,j,2);
				}
			}
		}
		actualitzarFilaAcabada(i);
	}
	
	public static void chetarColumna(int j, int [] trpf, int [] trpc, int [][] camp) {
		
		if (columnaAcabada [j]) return;
		
//		Primer completem la columna si ja no li falta cap tenda:
		if (trpc [j] == 0)
		{
			for (int i=0; i<n; ++i) omplir(camp, i, j, 2);
			return;
		}
		
		int capacitat = capacitat(columna(j,camp));
		int diferencia = capacitat - trpc[j];
		if (diferencia == 0)
		{
			int espaiForat = 0;
			for (int i=0; i<=n; ++i)
			{
				if (i<n && camp[i][j] == 0) ++espaiForat;
				else
				{
					if (espaiForat%2 == 1)
					{
						for (int k=0; k<(int) ((espaiForat+1)/2); ++k)
						{
							int pos = i-espaiForat+2*k;
							omplir(camp,pos,j,3);
							envoltar(camp,pos,j);
							++ tendesTrobades;
							-- trpf[pos];
							-- trpc[j];
						}
					}
					else
					{
						for (int k=0; k<espaiForat/2; ++k)
						{
							int pos = i-espaiForat+2*k;
							omplir(camp,pos,j-1,2);
							omplir(camp,pos,j+1,2);
							omplir(camp,pos+1,j-1,2);
							omplir(camp,pos+1,j+1,2);
						}
					}
					espaiForat = 0;
				}
			}
		}
		if (diferencia == 1)
		{
			for (int i=0; i<n; ++i)
			{
				int [] vec = columna(j,camp);
				omplir(vec, i-1, 2);
				omplir(vec, i, 2);
				omplir(vec, i+1, 2);
				if (capacitat(vec) < trpc[j])
				{
					omplir(camp,i,j-1,2);
					omplir(camp,i,j+1,2);
				}
			}
		}
		actualitzarColumnaAcabada(j);
	}
	
	public static void aparellaments() {
//		Cada tenda està aparellada amb un arbre. Haurem de fer servir aquesta dada com a tècnica
//		Per començar repassarem tots els arbres un per un i quantes caselles adjacents no descobertes tenen.
//		Cada cop que trobem una parella tenda + arbre, marquem com true el booleà aparellat en aquella posició.
		
		for (int i=0; i<posicioArbres.length; ++i)
		{
			for (int k=0; k<posicioArbres[i].length; ++k)
			{
//				Només ens interessen els arbres no aparellats. Si ho estan, sortim:
				int j = posicioArbres [i][k];
				if (parelles [i][j] > 0) continue;
				
				int g1 = 0;		// Nombre de caselles contígües amb una tenda desaparellada
				int g2 = 0; 	// Nombre de caselles contígües desconegudes
				int posx = i;	// Aquesta és la fila de la potencial tenda
				int posy = j;	// Aquesta és la columna de la potencial tenda
				
				if (j>0 	&& camp [i][j-1] == 3  	&& parelles [i][j-1] == -1)		{++ g1; posx = i; 	posy = j-1;}
				if (j<n-1 	&& camp [i][j+1] == 3 	&& parelles [i][j+1] == -1) 	{++ g1; posx = i; 	posy = j+1;}
				if (i>0 	&& camp [i-1][j] == 3 	&& parelles [i-1][j] == -1) 	{++ g1; posx = i-1;	posy = j;}
				if (i<n-1 	&& camp [i+1][j] == 3 	&& parelles [i+1][j] == -1)		{++ g1; posx = i+1;	posy = j;}
				
				if (j>0 	&& camp [i][j-1] == 0)									{++ g2; posx = i;	posy = j-1;}
				if (j<n-1 	&& camp [i][j+1] == 0) 									{++ g2; posx = i;	posy = j+1;}
				if (i>0 	&& camp [i-1][j] == 0) 									{++ g2; posx = i-1;	posy = j;}
				if (i<n-1 	&& camp [i+1][j] == 0) 									{++ g2; posx = i+1;	posy = j;}
				
//				En aquest cas, la casella amb la tenda desaparellada és la seva parella
				if (g1 == 1 && g2 == 0)
				{
					parelles [i][j] = nombreParelles;
					parelles [posx][posy] = nombreParelles;
					++ nombreParelles;
				}
				
//				En aquest cas, la casella desconeguda és tenda i és la seva parella
				if (g1 == 0 && g2 == 1)
				{
					parelles [i][j] = nombreParelles;
					parelles [posx][posy] = nombreParelles;
					++ nombreParelles;
					omplir(camp,posx,posy,3);
					envoltar(camp,posx,posy);
					++ tendesTrobades;
					-- trpf [posx];
					-- trpc [posy];
				}
				
//				En aquest cas, els arbres tenen exactament 2 caselles contígües desconegudes.
//				Com a conseqüencia, no hi ha té cap tenda contígua (per tant, g1 = 0).
//				Només ens quedarem amb el cas que les dues caselles desconegudes són NO oposades.
//				Com que la tenda haurà d'estar en una d'aquestes dues, podrem assegurar una casella de gespa.
				if (g1 == 0 && g2 == 2)
				{
					int x, y;
					ArrayList<Integer> posRow = new ArrayList<Integer> ();
					ArrayList<Integer> posCol = new ArrayList<Integer> ();
					
					if (j>0 	&& camp [i][j-1] == 0)	{posRow.add(i); posCol.add(j-1);}
					if (j<n-1 	&& camp [i][j+1] == 0) 	{posRow.add(i); posCol.add(j+1);}
					if (i>0 	&& camp [i-1][j] == 0)	{posRow.add(i-1); posCol.add(j);}							
					if (i<n-1 	&& camp [i+1][j] == 0) 	{posRow.add(i+1); posCol.add(j);}
					
					if (posRow.get(0) == posRow.get(1) || posCol.get(0) == posCol.get(1)) continue;
					
					if (posRow.get(0) != i) 	x = posRow.get(0);
					else						x = posRow.get(1);
					if (posCol.get(0) != j) 	y = posCol.get(0);
					else						y = posCol.get(1);
					
					omplir(camp,x,y,2);
				}
			}
		}
	}
	
	public static void identificarParelles() {
//		Aquesta funció s'aplicarà després de chetar files i columnes, per identificar parelles tent-tree
//		Primer buscarem entre totes les tendes desaparellades, i ens quedarem amb les que només tenen un arbre desaparellat contigu:
		for (int i=0; i<n; ++i)
		{
			for (int j=0; j<n; ++j)
			{
				if (camp[i][j] != 3 || parelles[i][j] > 0) continue;
				int g = 0;		// Nombre d'arbres contigus desaparellats
				int posx = i;	// Aquesta és la fila del potencial arbre parella
				int posy = j;	// Aquesta és la columna del potencial arbre parella
				if (j>0 	&& camp [i][j-1] == 1  	&& parelles [i][j-1] == -1)		{++ g; posx = i; 	posy = j-1;}
				if (j<n-1 	&& camp [i][j+1] == 1 	&& parelles [i][j+1] == -1) 	{++ g; posx = i; 	posy = j+1;}
				if (i>0 	&& camp [i-1][j] == 1 	&& parelles [i-1][j] == -1) 	{++ g; posx = i-1;	posy = j;}
				if (i<n-1 	&& camp [i+1][j] == 1 	&& parelles [i+1][j] == -1)		{++ g; posx = i+1;	posy = j;}
				if (g == 1)
				{
					parelles [i][j] = nombreParelles;
					parelles [posx][posy] = nombreParelles;
					++ nombreParelles;
				}
			}
		}
		
//		Ara fem el mateix amb els arbres desaparellats: ens quedem amb els que tenen només una tenda desaparellada contígua:
//		La diferència amb el bucle anterior és que ara hem de vigilar amb les caselles desconegudes. En cas d'una tenda al mig,
//		podem afirmar que les del voltant seran gespa (excepte els arbres), però en cas d'un arbre al mig i una tenda al seu costat,
//		hauríem de vigilar amb la casella del costat oposat a la tenda: si és desconeguda, podria haver-hi una altra tenda.
//		Per tant descartarem aquells arbres que tenen una tenda desaparellada i una casella desconeguda als costats.
		for (int i=0; i<n; ++i)
		{
			for (int k=0; k<posicioArbres[i].length; ++k)
			{
				int j = posicioArbres [i][k];
				if (parelles [i][j] > 0) continue;
				int tendes = 0;		// Nombre de tendes contígües desaparellades
				int posx = i;		// Aquesta és la fila de la potencial tenda parella
				int posy = j;		// Aquesta és la columna de la potencial tenda parella
				if (j>0 	&& camp [i][j-1] == 0)	continue;
				if (j<n-1 	&& camp [i][j+1] == 0) 	continue;
				if (i>0 	&& camp [i-1][j] == 0) 	continue;
				if (i<n-1 	&& camp [i+1][j] == 0)	continue;
				if (j>0 	&& camp [i][j-1] == 3  	&& parelles [i][j-1] == -1)		{++ tendes; posx = i; 	posy = j-1;}
				if (j<n-1 	&& camp [i][j+1] == 3 	&& parelles [i][j+1] == -1) 	{++ tendes; posx = i; 	posy = j+1;}
				if (i>0 	&& camp [i-1][j] == 3 	&& parelles [i-1][j] == -1) 	{++ tendes; posx = i-1;	posy = j;}
				if (i<n-1 	&& camp [i+1][j] == 3 	&& parelles [i+1][j] == -1)		{++ tendes; posx = i+1;	posy = j;}
				if (tendes != 1) continue;
				parelles [i][j] = nombreParelles;
				parelles [posx][posy] = nombreParelles;
				++ nombreParelles;
			}
		}
	}
	
}
