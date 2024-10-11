import java.util.Scanner;

public class IdentitatBezout
{
	public static void main(String[] args)
	{
		
		// CONDICIONS de funcionament: Nom�s demanem que a > 0, b > 0 i c >= 0
		// Resoldrem l'equaci� ax + by = c si i nom�s si estem sota aquestes condicions.
		// En cas que a = 0 o b = 0, l'equaci� no �s diof�ntica. Per tant, �s massa f�cil.
		// En cas que algun dels coeficients sigui negatiu, es pot convertir a m� f�cilment a coeficients positius.
		
		// L'equaci� t� soluci� si i nom�s si c �s m�ltiple de gcd(a,b) 
		// En aquest codi, x i y NO s�n les solucions de l'equaci� ax + by = c, sin� de ax + by = gcd(a,b)
		// Per tant, per trobar la soluci� particular de ax + by = c, fem x' = x*c/gcd(a,b) i y' = y*c/gcd(a,b)
		
		// INPUT: a, b, c
		// OUTPUT: gcd(a,b), x, y
		
		System.out.println("Introdueix els par�metres a b c (separats per un espai) de l'equaci� ax + by = c");
		Scanner s = new Scanner(System.in);
		int a = s.nextInt();
		int b = s.nextInt();
		int c = s.nextInt();
		int x, y, gcd;
		// int a = ;
		// int b = ;
		// int c = ;
		
		if (b == 0)
		{
			// En aquest cas, no cal que fem res
			// Posem x = y = gcd = 0 perqu� sin� no estar�em fent servir les variables.
			// De totes maneres, al final tenim un cas "especial" per a=0 o b=0.
			x = 0;
			y = 0;
			gcd = 0;
		}
		else if (a%b == 0)
		{
			x = 0;
			y = 1;
			gcd = b;
		}
		else
		{
			int [] q = new int [1000];
			int [] r = new int [1000];
		
			r [0] = a;
			r [1] = b;
			int i = 0;
			while (r [i+1] != 0)
			{
				q[i] = r[i] / r[i+1];
				r[i+2] = r[i] % r[i+1];
				++i;
			}
		
			gcd = Math.abs(r[i]);
		
			int [] [] coef = new int [i-1][2];
			coef [i-2][0] = 1;
			coef [i-2][1] = -q[i-2];
			for (int j = i-3; j >= 0; --j)
			{
				coef [j][0] = coef [j+1][1];
				coef [j][1] = coef [j+1][0] - coef [j+1][1] * q[j];
			}
			x = coef [0][0];
			y = coef [0][1];
		}
			
		if (a == 0 || b == 0)
			{
			System.out.println("Aquesta equaci� no �s ni diof�ntica.");
			System.out.println("De veritat no la saps resoldre?");
			}
		else if (a < 0 || b < 0 || c < 0)
			{
			System.out.println("Els coeficients a, b i c han de ser positius");
			}
		else if (c % gcd != 0)
			{
			System.out.println("Com que " + c + " no �s m�ltiple de gcd(" + a + ", " + b + ") = " + gcd + ",");
			System.out.println("l'equaci� " + a + "x + " + b + "y = " + c + " no t� soluci� entera.");
			}
		else
		{
			x = x * c / gcd;
			y = y * c / gcd;
			int kx = b / gcd;
			int ky = -a / gcd;
			
			System.out.println("Com que " + c + " �s m�ltiple de gcd(" + a + ", " + b + ") = " + gcd + ",");
			System.out.println("l'equaci� " + a + "x + " + b + "y = " + c + " t� soluci� entera, i �s");
			System.out.println("   x = " + x + " + " + kx + " K");
			System.out.println("   y = " + y + " + " + ky + " K");
			System.out.println("(on K pot prendre qualsevol valor enter)");
		}
	}
}