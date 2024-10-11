public class W1P7OK
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
	
	public static void main(String[] args)
	{
		
//		Aquí tenim la solució "correcta":
//		Hem de passar totes les strings a binari, i després fer el xor: P xor K = C
//		Finalment, el ciphertext C es torna a passar a hexadecimal.
		
		String P1 = "attack at dawn";
		String C1hex = "09e1c5f70a65ac519458e7e53f36";
		String P2 = "attack at dusk";

	    String P1bin = asciitobin(P1);
	    String P2bin = asciitobin(P2);
	    String C1bin = hextobin(C1hex);
	    String Kbin = xor(P1bin, C1bin);
	    String C2bin = xor(P2bin, Kbin);
	    String C2hex = bintohex(C2bin);
	    
//	    System.out.println(P1bin);
//	    System.out.println(P2bin);
//	    System.out.println(C1bin);
//	    System.out.println(Kbin);	
//	    System.out.println(C2bin);	
	    System.out.println(C2hex);	
	    
	}
}