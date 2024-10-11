public class W1P7KO
{
	public static void main(String[] args)
	{
		
//		Aquests resultats no es consideren bons pel problema
		
		String P1 = "attack at dawn";
		String C1 = "09e1c5f70a65ac519458e7e53f36";
		String P2 = "attack at dusk";
		StringBuffer K = new StringBuffer();
		StringBuffer C2 = new StringBuffer();
	
		int l = P1.length();
	    char[] P1cha = P1.toCharArray();
	    int [] Kint = new int[l];
	    for (int i = 0; i < l; i++)
	    {
	    	Kint [i] = (Integer.parseInt(C1.substring(2*i, 2*i+2), 16) - (int) P1cha[i] + 256) % 256;
//	    	System.out.println(Integer.toHexString(Kint[i]));
	    	K.append(Integer.toHexString(Kint[i]));
	    }
//	    System.out.println(K.toString());
	    
	    char[] P2cha = P2.toCharArray();
	    int [] C2int = new int[l];
	    for (int i = 0; i < l; i++)
	    {
	    	C2int [i] = ((int) P2cha[i] + Kint[i] + 256) % 256;
	    	if (C2int [i]/16 == 0) C2.append(0);
	    	C2.append(Integer.toHexString(C2int[i]));
//	    	System.out.println(Integer.toHexString(C2int[i]));
	    }
	    System.out.println(C2.toString());

	}
}
