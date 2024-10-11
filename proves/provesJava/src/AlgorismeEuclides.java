public class AlgorismeEuclides
{
	public static void main(String[] args)
	{
		// El programa retorna el càlcul de gcd(n,m)
		// També escriu tots els passos intermitjos
		int n = 244;
		int m = 88;
		
		int k = 0;
		if (n < m)
		{
			int i = m;
			m = n;
			n = i;
		}
		System.out.println("gcd(" + n + ", " + m + ") =");
		while (m != 0)
		{
			k = m;
			m = n % m;
			n = k;
			System.out.println("gcd(" + n + ", " + m + ") =");
		}
		int gcd = n;
		System.out.println(gcd);
	}
}