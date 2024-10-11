
public class PermutationDecrypt
{
	public static void main(String[] args)
	{
		// Ciphertext
		String C = "EAMEELTTMER";
		char [] Q = C.toCharArray();
		
		// Key (expressi� de la permutaci�)
		int [] K = {5,3,1,4,2};
		
		// Padding
		// Si volem codificaci� de l'espai, fem padding = 1 i escrivim el car�cter equivalent
		// Si no en volem, donem qualsevol altre valor al padding (t�pic: 0)
		int padding = 0;
		char pad = 'Z';
		
		StringBuffer P = new StringBuffer();
		char [][] L = new char [K.length][1 + Q.length / K.length];	
		
		// Comencem invertint la clau, �s a dir trobant la permutaci� inversa de K: Kinv
		int [] Kinv = new int [K.length];
		for (int i = 0; i < K.length; ++ i) Kinv[K[i]-1] = i+1;

		if (padding == 1)
		{
			// En aquest cas, Q.length �s m�ltiple de K.length
			for (int i = 0; i < K.length; ++ i)
			{
				for (int j = 0; j < Q.length / K.length; ++ j)
				{
					L[Kinv[i]-1][j] = Q[i * Q.length / K.length + j];
				}
			}
			
			for (int j = 0; j < Q.length / K.length; ++ j)
			{
				for (int i = 0; i < K.length; ++i)
				{
					if (L[i][j] != pad) P.append(L[i][j]);
				}
			}
		}
		
		else
		{
			// En aquest cas, Q.length no �s m�ltiple de K.length
			// Comen�arem calculant el nombre d'espais que hi ha:
			int k = 0;
			for (int i = 0; i < K.length; ++ i)
			{
				for (int j = 0; j < Q.length / K.length; ++ j)
				{
					L[Kinv[i]-1][j] = Q[k];
					++ k;
				}
				if (Kinv[i] > Q.length % K.length) L[Kinv[i]-1][Q.length / K.length] = pad;
				else
				{
					L[Kinv[i]-1][Q.length / K.length] = Q[k];
					++ k;
				}
			}
			for (int j = 0; j <= Q.length / K.length; ++ j)
			{
				for (int i = 0; i < K.length; ++i)
				{
					if (L[i][j] != pad) P.append(L[i][j]);
				}
			}
		}
		
		System.out.println(P);
	}
}
