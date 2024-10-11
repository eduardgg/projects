public class W1Assignment
{	
	
	public static String asciitobin (String ascii)
	{
		StringBuffer bin = new StringBuffer();
		char [] C = ascii.toCharArray();
	    for (int i = 0; i < C.length; ++i)
	    {
	    	String num = Integer.toBinaryString((int) C[i]);
	    	if (num.length() != 8)
	    	{
	    		for (int j = 0; j < 8 - num.length(); ++j) bin.append(0);
	    	}
	    	bin.append(num);
	    }
	    return bin.toString();
	}
	
	public static String asciitobin (char ascii)
	{
		StringBuffer bin = new StringBuffer();
	    String num = Integer.toBinaryString((int) ascii);
	    if (num.length() != 8)
	    {
	    	for (int j = 0; j < 8 - num.length(); ++j) bin.append(0);
	    }
	    bin.append(num);
	    return bin.toString();
	}
	
	public static String bintoascii (String bin)
	{
		StringBuffer ascii = new StringBuffer();
		for (int i = 0; i < bin.length() / 8; ++ i)
		{
			ascii.append((char) Integer.parseInt(bin.substring(8*i, 8*i+8), 2));
		}
		return ascii.toString();
	}
	
	public static String hextobin (String hex)
	{
		StringBuffer bin = new StringBuffer();
		for (int i = 0; i < hex.length(); ++ i)
		{
			String num = Integer.toBinaryString(Integer.parseInt(hex.substring(i, i+1), 16));
			if (num.length() != 4) {
				for (int j = 0; j < 4 - num.length(); ++ j) bin.append(0);
			}
			bin.append(num);
		}
		return bin.toString();
	}
	
	public static String bintohex (String bin)
	{
		StringBuffer hex = new StringBuffer();
		for (int i = 0; i < bin.length() / 4; ++ i)
		{
			String num = Integer.toHexString(Integer.parseInt(bin.substring(4*i, 4*i+4), 2));
			hex.append(num);
		}
		return hex.toString();
	}
	
	public static String xor (String A, String B)
	{
		// A i B han de ser paraules binàries de la mateixa longitud
		StringBuffer K = new StringBuffer();
		for (int i = 0; i < A.length(); ++ i)
		{
			K.append((Integer.parseInt(A.substring(i, i+1)) + Integer.parseInt(B.substring(i, i+1))) % 2);
		}
		return K.toString();
	}
	
	public static void separe (String A)
	{
		// A ha de ser una paraula binària de longitud múltiple de 8
		for (int i = 0; i < A.length() / 8; ++ i)
		{
			int num = i+1;
			System.out.println(num);
			System.out.println(" " + A.substring(8*i, 8*i+8));
		}
	}
	
	public static void main(String[] args)
	{
		
//		PARAULES COMPLETES (DADES DEL PROBLEMA)
		String [] M = new String [11];
		M[0] =  "32510ba9babebbbefd001547a810e67149caee11d945cd7fc81a05e9f85aac650e9052ba6a8cd8257bf14d13e6f0a803b54fde9e77472dbff89d71b57bddef121336cb85ccb8f3315f4b52e301d16e9f52f904";
		M[1] =  "315c4eeaa8b5f8aaf9174145bf43e1784b8fa00dc71d885a804e5ee9fa40b16349c146fb778cdf2d3aff021dfff5b403b510d0d0455468aeb98622b137dae857553ccd8883a7bc37520e06e515d22c954eba5025b8cc57ee59418ce7dc6bc41556bdb36bbca3e8774301fbcaa3b83b220809560987815f65286764703de0f3d524400a19b159610b11ef3e";
		M[2] =  "234c02ecbbfbafa3ed18510abd11fa724fcda2018a1a8342cf064bbde548b12b07df44ba7191d9606ef4081ffde5ad46a5069d9f7f543bedb9c861bf29c7e205132eda9382b0bc2c5c4b45f919cf3a9f1cb74151f6d551f4480c82b2cb24cc5b028aa76eb7b4ab24171ab3cdadb8356f";
		M[3] =  "32510ba9a7b2bba9b8005d43a304b5714cc0bb0c8a34884dd91304b8ad40b62b07df44ba6e9d8a2368e51d04e0e7b207b70b9b8261112bacb6c866a232dfe257527dc29398f5f3251a0d47e503c66e935de81230b59b7afb5f41afa8d661cb";
		M[4] =  "32510ba9aab2a8a4fd06414fb517b5605cc0aa0dc91a8908c2064ba8ad5ea06a029056f47a8ad3306ef5021eafe1ac01a81197847a5c68a1b78769a37bc8f4575432c198ccb4ef63590256e305cd3a9544ee4160ead45aef520489e7da7d835402bca670bda8eb775200b8dabbba246b130f040d8ec6447e2c767f3d30ed81ea2e4c1404e1315a1010e7229be6636aaa";
		M[5] =  "3f561ba9adb4b6ebec54424ba317b564418fac0dd35f8c08d31a1fe9e24fe56808c213f17c81d9607cee021dafe1e001b21ade877a5e68bea88d61b93ac5ee0d562e8e9582f5ef375f0a4ae20ed86e935de81230b59b73fb4302cd95d770c65b40aaa065f2a5e33a5a0bb5dcaba43722130f042f8ec85b7c2070";
		M[6] =  "32510bfbacfbb9befd54415da243e1695ecabd58c519cd4bd2061bbde24eb76a19d84aba34d8de287be84d07e7e9a30ee714979c7e1123a8bd9822a33ecaf512472e8e8f8db3f9635c1949e640c621854eba0d79eccf52ff111284b4cc61d11902aebc66f2b2e436434eacc0aba938220b084800c2ca4e693522643573b2c4ce35050b0cf774201f0fe52ac9f26d71b6cf61a711cc229f77ace7aa88a2f19983122b11be87a59c355d25f8e4";
		M[7] =  "32510bfbacfbb9befd54415da243e1695ecabd58c519cd4bd90f1fa6ea5ba47b01c909ba7696cf606ef40c04afe1ac0aa8148dd066592ded9f8774b529c7ea125d298e8883f5e9305f4b44f915cb2bd05af51373fd9b4af511039fa2d96f83414aaaf261bda2e97b170fb5cce2a53e675c154c0d9681596934777e2275b381ce2e40582afe67650b13e72287ff2270abcf73bb028932836fbdecfecee0a3b894473c1bbeb6b4913a536ce4f9b13f1efff71ea313c8661dd9a4ce";
		M[8] =  "315c4eeaa8b5f8bffd11155ea506b56041c6a00c8a08854dd21a4bbde54ce56801d943ba708b8a3574f40c00fff9e00fa1439fd0654327a3bfc860b92f89ee04132ecb9298f5fd2d5e4b45e40ecc3b9d59e9417df7c95bba410e9aa2ca24c5474da2f276baa3ac325918b2daada43d6712150441c2e04f6565517f317da9d3";
		M[9] =  "271946f9bbb2aeadec111841a81abc300ecaa01bd8069d5cc91005e9fe4aad6e04d513e96d99de2569bc5e50eeeca709b50a8a987f4264edb6896fb537d0a716132ddc938fb0f836480e06ed0fcd6e9759f40462f9cf57f4564186a2c1778f1543efa270bda5e933421cbe88a4a52222190f471e9bd15f652b653b7071aec59a2705081ffe72651d08f822c9ed6d76e48b63ab15d0208573a7eef027";
		M[10] = "466d06ece998b7a2fb1d464fed2ced7641ddaa3cc31c9941cf110abbf409ed39598005b3399ccfafb61d0315fca0a314be138a9f32503bedac8067f03adbf3575c3b8edc9ba7f537530541ab0f9f3cd04ff50d66f1d559ba520e89a2cb2a83";

//		L'objectiu del problema és desencriptar el primer ciphertext: M[0]. Els altres 10 textos són les "pistes".

//		Anem a passar a codi binari els textos
		for (int i = 0; i < 11; ++ i) M[i] = hextobin(M[i]);
//		Retallem els textos, per fer-los igual de llargs (la menor llargada és la del primer ciphertext)
		int longitud = M[0].length();
		for (int i = 1; i < 11; ++ i) if (M[i].length() < longitud) longitud = M[i].length();
		String [][] C = new String [11][83];
		for (int i = 0; i < 11; ++ i)
			for (int c = 0; c < longitud/8; ++ c)
				C[i][c] = M[i].substring(8*c, 8*c + 8);
		
//		La següent funció ens retornarà diverses línies.
//	    Com que C1 xor C2 = (M1 xor K) xor (M2 xor K) = M1 xor M2,
//		Cadascuna de les línies indica "diferències entre els caràcters situats en la mateixa posició de dues strings"
		
//		PAS 0: Creació de la matriu solució L (de caràcters) i inicialització en '?' (desconegut)
		char [][] T = new char [11][83];
		char [][] L = new char [11][83];
		for (int i = 0; i < 11; ++ i)
			for (int c = 0; c < 83; ++ c)
				T[i][c] = '?';
//		'?' significa desconegut completament
//		'S' significa signe (espai, punt, coma, guió, parèntesi, nombre...)
//		'L' significa lletra (majúscula o minúscula)

//		PAS 1: Localització dels signes en els ciphertexts (espais, punts, comes, guions...)
		for (int c = 0; c < 83; ++ c)
		{
			for (int i = 0; i < 11; ++ i)
			{
				int grau = 0;
				for (int j = 0; j < 11; ++ j)
				{
					if (Integer.parseInt(xor(C[i][c], C[j][c]).substring(1,2)) == 1) grau ++;
//					Tot això que ve és basura, ja que amb la introducció de "grau" no fa gens de falta
					/*
					if (T[i][c] == 'L')
					{
						if (Integer.parseInt(xor(C[i][c], C[j][c])) == 0) T[j][c] = 'L';
						if (Integer.parseInt(xor(C[i][c], C[j][c]).substring(1,2)) == 1) T[j][c] = 'S';
						continue;
					}
					if (T[j][c] == 'L')
					{
						if (Integer.parseInt(xor(C[i][c], C[j][c])) == 0) T[i][c] = 'L';
						if (Integer.parseInt(xor(C[i][c], C[j][c]).substring(1,2)) == 1) T[i][c] = 'S';
						continue;
					}
//					Si hem arribat aquí, vol dir que cap dels dos (ni Ci ni Cj) són coneguts com signe
//					En cas que sigui l'última j, si no s'ha demostrat fins aquí que L[i][c] no és un signe suposarem que sí que ho és
//					Crec que això que ve és merda (no considera més signes que l'espai)
					
					int n = Integer.parseInt(xor(C[i][c], C[j][c]).substring(1, 2));
					int m = Integer.parseInt(xor(C[i][c], C[j][c]));
					if (n == 0 && m != 0)
					{
						T[i][c] = 'L';
						T[j][c] = 'L';
					}
					*/
				}
				if (grau >= 6) T[i][c] = 'S';
				else T[i][c] = 'L';
			}
			
//			Podem prescindir de les línies a contínuació, ja que sembla que milloren molt poc el programa.
//			En aquest cas, canviaríem la línia "if (T[i][c] != ' ') continue;" per "if (T[i][c] != 'S') continue;"
//			La idea d'aquest codi és distingir entre espai i altres símbols, fent servir la freqüència.
//			És a dir, el símbol que més cops apareix, se suposa ser un espai.
//			POSSIBLE MILLORA: Distingir entre dos grups de símbols: els de més freqüència (ja que conté l'espai) són
//			els que comencen en 0010 i els que en tenen menys (contenen principalment nombres del 0 al 9) són 0011.
			
			int [] N = new int [256];
			for (int k = 0; k < 256; ++ k) N[k] = 0;
			int maxim = 0;
			for (int i = 0; i < 11; ++ i)
			{
				if (T[i][c] == 'S')
				{
					++ N[Integer.parseInt(C[i][c], 2)];
					if (N[Integer.parseInt(C[i][c], 2)] > N[maxim]) maxim = Integer.parseInt(C[i][c], 2);
				}
			} 
			String espai = asciitobin((char) maxim);
			for (int i = 0; i < 11; ++ i) {
				if (Integer.parseInt(C[i][c], 2) == Integer.parseInt(espai, 2)) T[i][c] = ' ';
			}
//			Fins aquí arriba el tram prescindible del codi.
		}
		
//		Amb això podem visualitzar la matriu L trobada recentment, amb '!', '?' o ' ':
		/*
		for (int i = 0; i < 11; ++ i)
		{
			for (int c = 0; c < 83; ++ c)
			{
				System.out.print (T[i][c]);
//				if (c != 82) System.out.print(" ");
			}
			System.out.println("");
		}
		*/
		
		String [] K = new String [83];
		for (int c = 0; c < 83; ++ c) K[c] = "?";
		for (int c = 0; c < 83; ++ c)
		{
//			Ara busquem la clau per cada caràcter c, usant els espais trobats anteriorment
			for (int i = 0; i < 11; ++ i)
			{
				if (T[i][c] != ' ') continue;
				// Estudiar diferents propietats dels signes per a distingir l'espai dels altres 
				// i definir la clau K només en cas que es conegui exactament que és un espai
				K[c] = xor(C[i][c], "00100000");
				break;
			}
		}
		
//		Visualitzem la contrassenya K trobada (en binari)
//		for (int c = 0; c < 83; ++ c) System.out.println(K[c]);
		
//		PAS 2: Ara usarem la clau només per les posicions on aquesta estigui trobada.
//		Això, si ho hem fet tot bé, hauria de ser les posicions on al menys un ciphertext hi té un espai.
		for (int c = 0; c < 83; ++ c)
		{
			if (K[c] == "?") continue;
			for (int i = 0; i < 11; ++ i) L[i][c] = bintoascii(xor(C[i][c], K[c])).charAt(0);
		}
		
//		PAS 3: Fem Output de la matriu de lletres trobades L
//		Cada fila és un text desxifrat diferent, i té una longitud de 83 caràcters.
		
//		/*
		for (int i = 0; i < 11; ++ i)
		{
			for (int c = 0; c < 83; ++ c)
			{
				if (K[c] != "?") System.out.print (L[i][c]);
				else System.out.print ('?');
//				if (c != 82) System.out.print(" ");
			}
			System.out.println("");
		}
//		*/
		
	}
}