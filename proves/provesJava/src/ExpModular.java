public class ExpModular
{
	
	public static int expMod (int base, int exp, int mod)
	{
		// El mòdul i l'exponent han de ser enters positius
		// La base ha de ser entera, i pot ser negativa
		if (exp == 1) return base % mod;
		if (base / mod != 0) return expMod(base % mod, exp, mod);
		if (exp % 2 == 0) return expMod(base * base, exp / 2, mod);
		return (base * expMod(base * base, exp / 2, mod)) % mod;
	}
	
	public static void main(String[] args)
	{
		// Resoldrem l'exponenciació modular b^p mod(m)
		int b = 5;
		int p = 3;
		int m = 13;
		int resultat = expMod(b,p,m);
		System.out.println(resultat);
	}
}
