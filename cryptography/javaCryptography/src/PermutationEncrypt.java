
public class PermutationEncrypt
{
	public static void main(String[] args)
	{
		// Plaintext
		String P = "JBBQJBIXQBO";
		char [] Q = P.toCharArray();
		
		// Key (expressió de la permutació)
		int [] K = {5,3,1,4,2};
		
		// Padding
		// Si volem codificació de l'espai, fem padding = 1 i escrivim el caràcter equivalent
		// Si no en volem, donem qualsevol altre valor al padding
		int padding = 0;
		char pad = 'Z';
		
		StringBuffer C = new StringBuffer();
		char [][] L = new char [K.length][1 + Q.length / K.length];

		for (int i = 0; i < K.length; ++ i)
		{
			for (int j = 0; j < 1 + Q.length / K.length; ++ j) 
			{
				if (i + j * K.length < Q.length) L[K[i]-1][j] = Q[i + j * K.length];
				else L[K[i]-1][j] = ' ';
			}
		}
		
		for (int i = 0; i < K.length; ++ i)
		{
			for (int j = 0; j < Q.length / K.length; ++ j) C.append(L[i][j]);
			if (L[i][Q.length / K.length] != ' ') C.append(L[i][Q.length / K.length]);
			else if ((padding == 1) && (Q.length % K.length != 0)) C.append(pad);
		}
		
		System.out.println(C);
	}
}
