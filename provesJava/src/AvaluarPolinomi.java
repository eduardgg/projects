
public class AvaluarPolinomi
{
	public static void main(String[] args)
	{
		
		// n = Grau del polinomi
		// x = Valor on avaluar el polinomi
		// v = Vector de tamany n+1. v[i] correspon al coeficient de grau i
		// En aquest exemple, definim el vector v = [1,2,3,4]: P(x) = 1+2x+3x^2+4x^3
		// El resultat ha de ser, per tant, 1+2*2+3*2^2+4*2^3 = 49
		
		int x = 2;
		int [] v = new int [] {1, 2, 3, 4};
		int n = v.length;
		int value = v[n-1];
		for (int i = n-2; i >= 0; --i)
		{
			value = x*value + v[i];
		}
		System.out.println(value);
	}
}
