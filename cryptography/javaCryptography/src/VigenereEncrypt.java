
public class VigenereEncrypt
{
	public static void main(String[] args)
	{
		// Plaintext (ha d'estar en majúscules)
		String P = "MEETMELATER";
		
		// Key (ha d'estar en majúscules)
		String K = "X";
		
		char [] M = new char[P.length()];
		
		for (int i = 0; i < P.length(); ++i)
		{
			if (P.charAt(i) == ' ')
				M[i] = ' ';
			else if (P.charAt(i) + K.charAt(i % K.length()) - 65 <= 90)
				M[i] = (char)(P.charAt(i) + K.charAt(i % K.length()) - 65);
			else
				M[i] = (char)(P.charAt(i) + K.charAt(i % K.length()) - 65 - 26);
		}
		
		// Cyphertext (OUTPUT)
		String C = new String (M);
		
		System.out.println(C);	
	}
}
