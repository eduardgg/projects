import java.io.UnsupportedEncodingException;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.security.PublicKey;
import java.io.ByteArrayInputStream;
import java.io.UnsupportedEncodingException;
import java.math.BigInteger;
import java.security.KeyFactory;
import java.security.KeyPair;
import java.security.KeyPairGenerator;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.security.PrivateKey;
import java.security.PublicKey;
import java.security.cert.CertificateFactory;
import java.security.interfaces.RSAPrivateKey;
import java.security.interfaces.RSAPublicKey;
import java.security.spec.EncodedKeySpec;
import java.security.spec.PKCS8EncodedKeySpec;
import java.security.spec.RSAPublicKeySpec;
import java.security.spec.X509EncodedKeySpec;
import java.util.Base64;
import javax.crypto.Cipher;

public class Validation
{
	
	private static String convertToHex(byte[] data) { 
		StringBuffer buf = new StringBuffer();
		for (int i = 0; i < data.length; i++) { 
			int halfbyte = (data[i] >>> 4) & 0x0F;
			int two_halfs = 0;
			do { 
				if ((0 <= halfbyte) && (halfbyte <= 9)) 
					buf.append((char) ('0' + halfbyte));
				else 
					buf.append((char) ('a' + (halfbyte - 10)));
				halfbyte = data[i] & 0x0F;
			} while(two_halfs++ < 1);
		} 
		return buf.toString();
	}    
	
	public static String SHA(byte[] convertme) throws NoSuchAlgorithmException{
	    MessageDigest md = MessageDigest.getInstance("SHA-1"); 
	    return convertToHex(md.digest(convertme));
	}
	
//	public static String SHA1v1(String input) throws Exception
//	{
//        MessageDigest mDigest = MessageDigest.getInstance("SHA1");
//        byte[] result = mDigest.digest(input.getBytes());
//        StringBuffer sb = new StringBuffer();
//        for (int i = 0; i < result.length; i++) {
//            sb.append(Integer.toString((result[i] & 0xff) + 0x100, 16).substring(1));
//        }
//         
//        return sb.toString();
//    }
//	
//	public static String SHA1v2(byte[] convertme) {
//	    MessageDigest md = null;
//	    try {
//	        md = MessageDigest.getInstance("SHA-1");
//	    }
//	    catch(NoSuchAlgorithmException e) {
//	        e.printStackTrace();
//	    } 
//	    return new String(md.digest(convertme));
//	}
	
    public static KeyPair buildKeyPair() throws NoSuchAlgorithmException
    {
        final int keySize = 2048;
        KeyPairGenerator keyPairGenerator = KeyPairGenerator.getInstance("RSA");
        keyPairGenerator.initialize(keySize);      
        return keyPairGenerator.genKeyPair();
    }
    
    public static byte[] encrypt(PrivateKey privateKey, String message) throws Exception
    {
        Cipher cipher = Cipher.getInstance("RSA");  
        cipher.init(Cipher.ENCRYPT_MODE, privateKey);
        return cipher.doFinal(message.getBytes());  
    }
    
    public static byte[] decrypt(PublicKey publicKey, byte [] encrypted) throws Exception
    {
        Cipher cipher = Cipher.getInstance("RSA");  
        cipher.init(Cipher.DECRYPT_MODE, publicKey);
        return cipher.doFinal(encrypted);
    }
    
    public static byte[] encryptByPublicKey(byte[] data, byte[] key) throws Exception
    {
    	X509EncodedKeySpec x509KeySpec = new X509EncodedKeySpec(key);
    	KeyFactory keyFactory = KeyFactory.getInstance("RSA");
    	PublicKey publicKey = keyFactory.generatePublic(x509KeySpec);

    	Cipher cipher = Cipher.getInstance(keyFactory.getAlgorithm());
    	cipher.init(Cipher.ENCRYPT_MODE, publicKey);
    	return cipher.doFinal(data);
    }
    
    public static byte[] RSAencrypt(BigInteger mod, BigInteger exp, byte [] data) throws Exception
    {
		KeyFactory keyFactory = KeyFactory.getInstance("RSA");
		RSAPublicKeySpec pubKeySpec = new RSAPublicKeySpec(mod, exp);
		RSAPublicKey key = (RSAPublicKey) keyFactory.generatePublic(pubKeySpec);
		Cipher cipher = Cipher.getInstance("RSA/ECB/NoPadding");
		cipher.init(Cipher.ENCRYPT_MODE, key);
		byte[] cipherData = cipher.doFinal(data);
		return cipherData;
    }
    
	public static void main(String [] args) throws Exception
	{
		
		byte exp [] = {37};
		
		byte mod [] =
		{
			-42 ,-9  ,19  ,62  ,-110,23  ,24  ,90  ,
			-66 ,-89 ,-91 ,-93 ,-127,-3  ,60  ,20  ,
			-95 ,-46 ,87  ,-111,-74 ,87  ,124 ,-42 ,
			85  ,8   ,59  ,36  ,-47 ,59  ,-31 ,-21 ,
			19  ,-4  ,96  ,76  ,-128,44  ,-52 ,42  ,
			40  ,57  ,119 ,-62 ,-93 ,20  ,30  ,-1  ,
			30  ,115 ,-94 ,-123,111 ,-54 ,-17 ,12  ,
			35  ,-35 ,68  ,-111,46  ,102 ,8   ,-124,
			25  ,-47 ,-109,89  ,86  ,81  ,80  ,-106,
			-123,-97 ,85  ,80  ,-80 ,20  ,-60 ,104 ,
			-70 ,-88 ,-55 ,29  ,110 ,86  ,-34 ,-73 ,
			73  ,32  ,11  ,49  ,67  ,-115,37  ,-89 ,
			-31 ,-56 ,59  ,39  ,83  ,7   ,-80 ,-78 ,
			-11 ,88  ,28  ,38  ,44  ,105 ,-98 ,-93 ,
			-20 ,63  ,-34 ,33  ,54  ,-23 ,21  ,-89 ,
			28  ,-32 ,-21 ,24  ,-85 ,62  ,40  ,113	
		};
			
		byte Targeta [] =
		{
			9,-113,-47,87,-77,118,3,-20,60,-19,-87,-104,-52,65,-16,-44,
			-9,-95,-84,-106,87,27,116,108,-121,-89,-99,100,96,97,-108,-16,
			48,4,-125,120,122,78,90,-71,66,30,-13,-106,-39,-110,-38,-10,
			-63,-63,7,44,-16,14,55,-12,-14,-58,21,-54,-58,63,-8,-92,
			-1,-62,98,117,31,25,-87,-61,-127,104,44,-123,-109,83,-125,-99,
			72,-118,113,73,-81,-13,28,-10,-9,-53,-39,-42,-103,-102,-71,-42,
			-122,-71,-30,-30,46,99,77,-127,35,102,54,-93,86,-20,67,41,
			65,-98,98,-51,100,-33,94,27,125,-17,22,-75,5,108,64,-23,
			37,-120,-6,-55,-17,-127,54,120,-22,-29,118,87,-70,-3,75,83,
			53,24,75,15,-69,19,-55,-12,-45,56,-117,41,-15,6,81,-51,
			71,54,81,-38,-5,120,71,45,42,69,-78,-30,-117,-78,-80,-8,
			121,65,65,52,55,56,86,32,56,51,49,98,32,79,80,32,
			48,50,47,48,57,47,50,48,49,54,32,48,52,58,50,49,
			-122,-48,85,102,2,91,-37,102,28,-68,-115,121,80,14,99,-102,
			-79,-13,-116,-57,-37,104,-118,-21,-17,19,-58,-118,-127,90,-41,117,
			86,-55,-73,-80,50,112,58,43,-52,-59,26,-33,-92,-16,-47,-31
		};
			
		byte PROds [] = new byte [128];
		byte PROexp [] = new byte [1];
		byte PROmod [] = new byte [48];
		byte PROpub [] = new byte [49];
		byte SUPinfo [] = new byte [31];
		byte SUPds [] = new byte [48];
		
		for (int i = 0; i < 128; ++ i) PROds [i] = Targeta [i];
		for (int i = 0; i < 1; ++ i) PROexp [i] = Targeta [i + 128];
		for (int i = 0; i < 48; ++ i) PROmod [i] = Targeta [i + 129];
		for (int i = 0; i < 49; ++ i) PROpub [i] = Targeta [i + 128];
		for (int i = 0; i < 31; ++ i) SUPinfo [i] = Targeta [i + 177];
		for (int i = 0; i < 48; ++ i) SUPds [i] = Targeta [i + 208];
		
//		----------------------------------------------------------------------------------------------
		
//		1a PART: Validaci� del Prove�dor
		
		
		BigInteger modulus = new BigInteger (convertToHex(mod), 16);
		BigInteger exponent = new BigInteger (convertToHex(exp), 16);
		
//		String decryptPROds = convertToHex(RSAencrypt(modulus, exponent, PROds)).substring(216,256);
//		String hashPROpub = convertToHex(toSHA1(PROpub).getBytes());
		
//		- Tamb� funciona si programem manualment l'exponenciaci� modular:
		BigInteger base1 = new BigInteger (convertToHex(PROds), 16);
		BigInteger remainder1 = base1.modPow(exponent, modulus);
		String decryptPROds = convertToHex(remainder1.toByteArray());
		decryptPROds = decryptPROds.substring(decryptPROds.length() - 40, decryptPROds.length());
		String hashPROpub = SHA(PROpub);
		
//		- Fem display dels resultats:
		System.out.println("Validation of Provider : " + (decryptPROds.equals(hashPROpub)));
		System.out.println(decryptPROds);
		System.out.println(hashPROpub);
		
		System.out.println();
		
//		----------------------------------------------------------------------------------------------	
		
//		2a PART: Validaci� de la informaci� del supply
		

		BigInteger PROmodulus = new BigInteger (convertToHex(PROmod), 16);
		BigInteger PROexponent = new BigInteger (convertToHex(PROexp), 16);
		
//		String decryptSUPds = convertToHex(RSAencrypt(PROmodulus, PROexponent, SUPds)).substring(216,256);
//		String hashSUPinfo = convertToHex(toSHA1(SUPinfo).getBytes());
		
//		- PROBLEMA! La lliberia anterior no permet usar claus de longitud menor a 512 bits (aquesta en t� 384)
//		- Haurem de programar "manualment" una exponenciaci� modular amb Big Integers:
		BigInteger base2 = new BigInteger (convertToHex(SUPds), 16);
		BigInteger remainder2 = base2.modPow(PROexponent, PROmodulus);
		String decryptSUPds = convertToHex(remainder2.toByteArray());
		decryptSUPds = decryptSUPds.substring(decryptSUPds.length() - 40, decryptSUPds.length());
		String hashSUPinfo = SHA(SUPinfo);
		
//		- Fem display dels resultats:
		System.out.println("Validation of Supply Information : " + (decryptSUPds.equals(hashSUPinfo)));
		System.out.println(decryptSUPds);
		System.out.println(hashSUPinfo);
		
//		----------------------------------------------------------------------------------------------
		
    }
}
