
public class VigenereDecrypt
{
	public static void main(String[] args)
	{
		// Cyphertext (ha d'estar en majúscules)
		String C = "DTXSAOMP";
		
		// Key (ha d'estar en majúscules)
		String K = "LEMON";
		
		char [] M = new char[C.length()];
		
		for (int i = 0; i < C.length(); ++i)
		{
			if (C.charAt(i) == ' ')
				M[i] = ' ';
			else if (C.charAt(i) - K.charAt(i % K.length()) + 65 >= 65)
				M[i] = (char)(C.charAt(i) - K.charAt(i % K.length()) + 65);
			else
				M[i] = (char)(C.charAt(i) - K.charAt(i % K.length()) + 65 + 26);
		}
		
		// Plaintext (OUTPUT)
		String P = new String (M);
		
		System.out.println(P);
				
	}
}
