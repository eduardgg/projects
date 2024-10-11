public class Conversions
{
	public static void main(String[] args)
	{	
		
//		--------------------------------------------------------------
//
//		// CONVERSIONS
//		
//		
//		// Hexadecimal to Decimal
//		String hexNumber = "17b";
//		int decimal = Integer.parseInt(hexNumber, 16);
//		System.out.println(decimal);
//		
//		
//		// Decimal to Hexadecimal
//		Integer decimal = 43981;
//		String hexNumber = Integer.toHexString(decimal);
//		System.out.println(hexNumber);
//		
//		
//		// Hexadecimal to Binary
//	    String hex = "75544d";
//	    String bin = Integer.toBinaryString(Integer.parseInt(hex, 16)); 
//	    System.out.println(bin.toString());
//	    
//		
//		// Binary to Hexadecimal
//		String bin = "11101010101010001001101";
//		String hex = Integer.toHexString(Integer.parseInt(bin, 2)); 
//	    System.out.println(hex.toString());
//	    
//	    
//		// Hexadecimal to ASCII
//		String hex = "75544d";
//		StringBuilder output = new StringBuilder();
//	    for (int i = 0; i < hex.length(); i += 2)
//	    {
//	        String str = hex.substring(i, i+2);
//	        output.append((char)Integer.parseInt(str, 16));
//	    }
//	    System.out.println(output.toString());
//	    
//	    		
//	    // ASCII to Hexadecimal
//		String asciiValue = "Eduardo";
//	    char[] chars = asciiValue.toCharArray();
//	    StringBuffer hex = new StringBuffer();
//	    for (int i = 0; i < chars.length; i++)
//	    {
//	        hex.append(Integer.toHexString((int) chars[i]));
//	    }
//	    System.out.println(hex.toString());
//	    
//
//		// ASCII to Byte or Integer
//		String cadena = "I am a string";
//		byte [] bytes = cadena.getBytes();
//		System.out.println(bytes);
//		int [] numeros = new int [bytes.length];
//		for (int i = 0; i < bytes.length; ++ i)
//		{
//			numeros [i] = (int) bytes [i];
//			System.out.println(numeros [i]);
//		}
//		
//		
//		// Hexadecimal to Byte
//		int hex = 0x45;
//		byte hexbytejat = (byte) hex;
//		System.out.println(hexbytejat);
//		
//		
//		// Byte to Hexadecimal
//		private static String convertToHex(byte[] data) { 
//			StringBuffer buf = new StringBuffer();
//			for (int i = 0; i < data.length; i++) { 
//				int halfbyte = (data[i] >>> 4) & 0x0F;
//				int two_halfs = 0;
//				do { 
//					if ((0 <= halfbyte) && (halfbyte <= 9)) 
//						buf.append((char) ('0' + halfbyte));
//					else 
//						buf.append((char) ('a' + (halfbyte - 10)));
//					halfbyte = data[i] & 0x0F;
//				} while(two_halfs++ < 1);
//			} 
//			return buf.toString();
//		}
//		
//		
//		// Byte Array to String (text)
//		byte[] text = "This is a secret message.".getBytes();
//		String S = new String (text); 
//	    System.out.println(new String(text));
//	    System.out.println(S);
//				
//		
//		// Extract Char from a String
//		String cadena = "I am a string";
//		char C = cadena.charAt(4);
//		System.out.println(C);
//
//		
//		// Extract String from a String
//		String cadena = "I am a string";
//		String nova = cadena.substring(3,4);
//		System.out.println(nova);
//		
//		
//		// String to Char Array
//		String cadena = "I am a string";
//		char [] cadchars = cadena.toCharArray();
//		System.out.println(cadchars[9]);
//		
//		
//		--------------------------------------------------------------
		
	}
}