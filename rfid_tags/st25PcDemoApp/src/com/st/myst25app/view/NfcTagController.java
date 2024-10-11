package com.st.myst25app.view;
import java.math.BigInteger;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.ArrayList;
import java.util.List;
import java.util.Timer;
import java.util.TimerTask;

import com.st.myst25app.MainApp;
import com.st.st25sdk.Helper;
import com.st.st25sdk.NFCTag;
import com.st.st25sdk.NFCTag.NfcTagTypes;
import com.st.st25sdk.RFReaderInterface;
import com.st.st25sdk.STException;
import com.st.st25sdk.TagHelper;
import com.st.st25sdk.TagHelper.ProductID;
import com.st.st25sdk.command.Iso15693Command;
import com.st.st25sdk.command.Iso15693Protocol;
import com.st.st25sdk.iso14443sr.ST25TB04KTag;
import com.st.st25sdk.type4a.m24srtahighdensity.ST25TA64KTag;
import com.st.st25sdk.type4a.st25ta.ST25TA02KDTag;
import com.st.st25sdk.type4a.st25ta.ST25TA02KPTag;
import com.st.st25sdk.type5.STType5Tag;
import com.st.st25sdk.type5.Type5Tag;
import com.st.st25sdk.type5.lri.LRi2KTag;
import com.st.st25sdk.type5.lri.LRiS2KTag;
import com.st.st25sdk.type5.m24lr.LRiS64KTag;
import com.st.st25sdk.type5.st25dv.ST25DVTag;
import com.st.st25sdk.type5.st25dv.ST25TV64KTag;
import com.st.st25sdk.type5.st25tv.ST25TVTag;

import javafx.application.Platform;
import javafx.beans.property.SimpleStringProperty;
import javafx.beans.property.StringProperty;
import javafx.beans.value.ChangeListener;
import javafx.beans.value.ObservableValue;
import javafx.collections.FXCollections;
import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.control.ChoiceBox;
import javafx.scene.control.Label;
import javafx.scene.control.TextArea;

public class NfcTagController {
	// GUI elements
	@FXML private Button discoverButton;
	@FXML private ChoiceBox tagTypeBox;	
	@FXML private Label tagUidLabel;
	@FXML private Label tagSizeLabel;
	@FXML private Label readerStatusLabel;
	@FXML private Label providerVerificationLabel;
	@FXML private Label supplyVerificationLabel;
	@FXML private Label partNumberLabel;
	@FXML private Label selectabilityLabel;
	@FXML private Label colorLabel;
	@FXML private Label manufacturingDateLabel;
	@FXML private Label manufacturingTimeLabel;
	@FXML private Button writeButton;
	@FXML private ChoiceBox dataTypeBox;
	@FXML private TextArea dataArea;
	@FXML private Label writeStatusLabel;

	// Reference to the main application
	private MainApp mainApp;
	// List of detected tag UIDs
	private List<byte[]> uidList = new ArrayList<>();
	private NFCTag recognizedNFCTag = null;
	private StringProperty firstTagUid = new SimpleStringProperty();
	private StringProperty firstTagSize = new SimpleStringProperty();
	public String tipusData = "Hexadecimal";
	public String tipusTag = "4A";
	// Aqu� escrivim el tipus del tag ("5" o "4A")
	// Per defecte el posem a 4A
	/**
	 * Initializes the controller class.
	 * This method is automatically called after the fxml file is loaded.
	 */	
	@FXML
	public void initialize () throws NoSuchAlgorithmException{
		tagUidLabel.setText("");
		tagSizeLabel.setText("");
		providerVerificationLabel.setText("");
		supplyVerificationLabel.setText("");
		partNumberLabel.setText("");
		selectabilityLabel.setText("");
		colorLabel.setText("");
		manufacturingDateLabel.setText("");
		manufacturingTimeLabel.setText("");
		readerStatusLabel.setText("No reader is connected");
		writeStatusLabel.setText("");
		tagTypeBox.setItems(FXCollections.observableArrayList("Type 4A", "Type 4B", "Type 5"));
		tagTypeBox.getSelectionModel().selectedIndexProperty().addListener(new ChangeListener <Number> () {
			public void changed(ObservableValue ov, Number value, Number new_value) {
				switch (new_value.intValue()) {
				case 0: tipusTag = "4A"; break;
				case 1: tipusTag = "4B"; break;
				case 2: tipusTag = "5";  break;
				default: break;
				}
			}
		});
		dataTypeBox.setItems(FXCollections.observableArrayList("ASCII", "Binary", "Hexadecimal"));
		dataTypeBox.getSelectionModel().selectedIndexProperty().addListener(new ChangeListener <Number> () {
			public void changed(ObservableValue ov, Number value, Number new_value) {
				switch (new_value.intValue()) {
				case 0: tipusData = "ASCII"; break;
				case 1: tipusData = "Binary"; break;
				case 2: tipusData = "Hexadecimal";  break;
				default: break;
				}
			}
		});
		discoverButton.setOnAction((event) -> {
			Timer timer = new Timer();
			TimerTask timerTask = new TimerTask() {
				@Override
	            public void run() {
					Platform.runLater(() -> {
	                try {
	    				startDiscoveryProcess();
	    				updateUidLabel(uidList);
	    				updateSizeLabel(uidList);
	    				validateNdef();
	    			} catch (NoSuchAlgorithmException e) {
	    				e.printStackTrace();
	    			}
	                // Bind tag's UID label content to the value found in the first element of the inventory list
	    			tagUidLabel.textProperty().bind(firstTagUid);
	    			// Bind tag's size label content to the value found in the first element of the inventory list
	    			tagSizeLabel.textProperty().bind(firstTagSize);
					});
	            }
			};
			timer.scheduleAtFixedRate(timerTask, 1000, 3000);
		});
		writeButton.setOnAction(event -> updateWriteStatus(writeToTag()));
	}
	/**
	 * setMainApp is called by the main application to give a reference of itself to the controller.
	 *
	 * @param mainApp
	 */
	public void setMainApp(MainApp mainApp) {
		this.mainApp = mainApp;
		// Bind reader connection status to a label that displays the updated value whenever there is a change
		readerStatusLabel.textProperty().bind(mainApp.readerStatusProperty());
	}
	public void startDiscoveryProcess() throws NoSuchAlgorithmException {
		// Empty lists of detected tags
		uidList.clear();
		try {
			// Call reader's 15693 anti-collision algorithm
			if (tipusTag.equals("4A")) {
				uidList =
				mainApp.mActiveRFReader.getTransceiveInterface().inventory(RFReaderInterface.InventoryMode.NFC_TYPE_4A);
			}
			if (tipusTag.equals("4B")) {
				uidList =
				mainApp.mActiveRFReader.getTransceiveInterface().inventory(RFReaderInterface.InventoryMode.NFC_TYPE_4B);
			}
			if (tipusTag.equals("5")) {
				uidList =
				mainApp.mActiveRFReader.getTransceiveInterface().inventory(RFReaderInterface.InventoryMode.NFC_TYPE_5);
			}
		} catch (STException e) {
			e.printStackTrace();
		}
		resetTags();
	}
	/**
	 * The Inventory implementation on the RF reader may use the anti-collision algorithm
	 * and send the "Stay Quiet" command to a tag once detected.
	 * resetTags() sends the "Reset to Ready" command to all tags in order to reset them to the ready state.
	 */
	public void resetTags() {
		// Create a command pool object containing all Iso15693 commands
		try {
			Iso15693Command cmd = new Iso15693Command(mainApp.mActiveRFReader.getTransceiveInterface(), null);
			if (!uidList.isEmpty()) {
				cmd.setFlag(Iso15693Protocol.HIGH_DATA_RATE_MODE);
				cmd.resetToReady();
			}
		} catch (STException e) {
			e.printStackTrace();
		}
	}
	/**
	 * Updates tagUidLabel with the UID string of the first element in the inventory list.
	 * This function first reverses the byte array containing the UID then converts it into a String.
	 */
	public void updateUidLabel(List<byte[]> myList) {
		if (myList.isEmpty()) {
//			firstTagUid.set("No tag discovered");
			providerVerificationLabel.setText("");
			supplyVerificationLabel.setText("");
			partNumberLabel.setText("");
			selectabilityLabel.setText("");
			colorLabel.setText("");
			manufacturingDateLabel.setText("");
			manufacturingTimeLabel.setText("");
		} else {
			firstTagUid.set(Helper.convertByteArrayToHexString(Helper.reverseByteArray(myList.get(0))));
		}
	}
	/**
	 * Updates tagSizeLabel with Size of the first element in the inventory list
	 */
	public void updateSizeLabel(List<byte[]> myList) {
		if (myList.isEmpty()) {
//			firstTagSize.set("");
			providerVerificationLabel.setText("");
			supplyVerificationLabel.setText("");
			partNumberLabel.setText("");
			selectabilityLabel.setText("");
			colorLabel.setText("");
			manufacturingDateLabel.setText("");
			manufacturingTimeLabel.setText("");
		} else {
			try {
				if (tipusTag.equals("5")) recognizedNFCTag = identifyTag(Helper.reverseByteArray(myList.get(0)));
				if (tipusTag.equals("4A")) recognizedNFCTag = identifyTag(myList.get(0));
				if (tipusTag.equals("4B")) recognizedNFCTag = identifyTag(myList.get(0));
				if (recognizedNFCTag != null) {
					firstTagSize.set(String.valueOf(recognizedNFCTag.getMemSizeInBytes() * 8) + " bits (" +
							String.valueOf(recognizedNFCTag.getMemSizeInBytes() * 8 / 1024) + " Kbit)");
				} else {
					firstTagSize.set("Tag could not be recognized");
				}
			} catch (STException e) {
				firstTagSize.set("Memory size data could not be extracted");
			}
		}
	}
	public NFCTag identifyTag(byte[] uid) throws STException {
		ProductID productName;
		RFReaderInterface readerInterface = mainApp.mActiveRFReader.getTransceiveInterface();
		NfcTagTypes tagType = readerInterface.decodeTagType(uid);
		if (tagType == NfcTagTypes.NFC_TAG_TYPE_V) {
			productName = TagHelper.identifyTypeVProduct(readerInterface, uid);
		} else if (tagType == NfcTagTypes.NFC_TAG_TYPE_4A) {
			productName = TagHelper.identifyType4Product(readerInterface, uid);
		} else if (tagType == NfcTagTypes.NFC_TAG_TYPE_4B) {
			productName = TagHelper.identifyType4Product(readerInterface, uid);
		} else {
			productName = TagHelper.identifyProduct(readerInterface, uid);
		}
		switch (productName) {
		/************** SELECTION OF TYPE 5 PRODUCTS *************/
		case PRODUCT_ST_ST25DV04K_I:
		case PRODUCT_ST_ST25DV04K_J:
		case PRODUCT_ST_ST25DV16K_I:
		case PRODUCT_ST_ST25DV16K_J:
		case PRODUCT_ST_ST25DV64K_I:
		case PRODUCT_ST_ST25DV64K_J:
			recognizedNFCTag = new ST25DVTag(readerInterface, uid);
			recognizedNFCTag.setName(productName.toString());
			break;
		case PRODUCT_ST_ST25TV02K:
			recognizedNFCTag = new ST25TVTag(readerInterface, uid);
			recognizedNFCTag.setName(productName.toString());
			break;
		case PRODUCT_ST_ST25TV64K:
			recognizedNFCTag = new ST25TV64KTag(readerInterface, uid);
			recognizedNFCTag.setName(productName.toString());
			break;
		case PRODUCT_ST_LRi2K:
			recognizedNFCTag = new LRi2KTag(readerInterface, uid);
			recognizedNFCTag.setName(productName.toString());
			break;
		case PRODUCT_ST_LRiS2K:
			recognizedNFCTag = new LRiS2KTag(readerInterface, uid);
			recognizedNFCTag.setName(productName.toString());
			break;
		case PRODUCT_ST_LRiS64K:
			recognizedNFCTag = new LRiS64KTag(readerInterface, uid);
			recognizedNFCTag.setName(productName.toString());
			break;
		case PRODUCT_ST_ST25TA02K_D:
			recognizedNFCTag = new ST25TA02KDTag(readerInterface, uid);
			recognizedNFCTag.setName(productName.toString());
			break;
		case PRODUCT_ST_ST25TA02K_P:
			recognizedNFCTag = new ST25TA02KPTag(readerInterface, uid);
			recognizedNFCTag.setName(productName.toString());
			break;
		case PRODUCT_ST_ST25TA64K:
			recognizedNFCTag = new ST25TA64KTag(readerInterface, uid);
			recognizedNFCTag.setName(productName.toString());
			break;
		case PRODUCT_ST_ST25TB04K:
			recognizedNFCTag = new ST25TB04KTag(readerInterface, uid);
			recognizedNFCTag.setName(productName.toString());
			break;
		case PRODUCT_GENERIC_TYPE5_AND_ISO15693:
			// Non ST or unrecognized Iso15693 products
			recognizedNFCTag = new STType5Tag(readerInterface, uid);
			recognizedNFCTag.setName(productName.toString());
			break;
		case PRODUCT_GENERIC_TYPE5:
			// Non ST or unrecognized NFC type 5 products
			recognizedNFCTag = new Type5Tag(readerInterface, uid);
			recognizedNFCTag.setName(productName.toString());
			break;
		default:
			break;
		}
		return recognizedNFCTag;
	}
	public void validateNdef() throws NoSuchAlgorithmException {
		// Aqu� llegim el tag i fem la comprovaci� de la signatura digital.
		// Si tot queda comprovat correctament, procedirem a donar la informaci� del supply.
		if (recognizedNFCTag != null) {
			try {
				
				byte [] Card = recognizedNFCTag.readBytes(0x0000, 256);
				
				byte PROds [] = new byte [128];
				byte PROexp [] = new byte [1];
				byte PROmod [] = new byte [48];
				byte PROpub [] = new byte [49];
				byte SUPinfo [] = new byte [31];
				byte SUPds [] = new byte [48];
				
				for (int i = 0; i < 128; ++ i) PROds [i] = Card [i];
				for (int i = 0; i < 1; ++ i) PROexp [i] = Card [i + 128];
				for (int i = 0; i < 48; ++ i) PROmod [i] = Card [i + 129];
				for (int i = 0; i < 49; ++ i) PROpub [i] = Card [i + 128];
				for (int i = 0; i < 31; ++ i) SUPinfo [i] = Card [i + 177];
				for (int i = 0; i < 48; ++ i) SUPds [i] = Card [i + 208];
				
				byte number [] = new byte [6];
				byte selectability [] = new byte [4];
				byte color [] = new byte [2];
				byte month [] = new byte [2];
				byte day [] = new byte [2];
				byte year [] = new byte [4];
				byte hour [] = new byte [2];
				byte minute [] = new byte [2];
				
				for (int j = 0; j < 6; ++ j) number [j] = SUPinfo [j];
				for (int j = 0; j < 4; ++ j) selectability [j] = SUPinfo [j + 7];
				for (int j = 0; j < 2; ++ j) color [j] = SUPinfo [j + 12];
				for (int j = 0; j < 2; ++ j) month [j] = SUPinfo [j + 15];
				for (int j = 0; j < 2; ++ j) day [j] = SUPinfo [j + 18];
				for (int j = 0; j < 4; ++ j) year [j] = SUPinfo [j + 21];
				for (int j = 0; j < 2; ++ j) hour [j] = SUPinfo [j + 26];
				for (int j = 0; j < 2; ++ j) minute [j] = SUPinfo [j + 29];
				
				// PART 1: Validaci� del prove�dor:
				BigInteger HPmodulus = new BigInteger (byteToHex(HPmod), 16);
				BigInteger HPexponent = new BigInteger (byteToHex(HPexp), 16);
				BigInteger base1 = new BigInteger (byteToHex(PROds), 16);
				BigInteger remainder1 = base1.modPow(HPexponent, HPmodulus);
				String decryptPROds = byteToHex(remainder1.toByteArray());
				decryptPROds = decryptPROds.substring(decryptPROds.length() - 40, decryptPROds.length());
				String hashPROpub = SHA(PROpub);
				if (decryptPROds.equals(hashPROpub)) providerVerificationLabel.setText("Correct");
				else providerVerificationLabel.setText("Incorrect");
				
				// PART 2: Validaci� del supply:
				BigInteger PROmodulus = new BigInteger (byteToHex(PROmod), 16);
				BigInteger PROexponent = new BigInteger (byteToHex(PROexp), 16);
				BigInteger base2 = new BigInteger (byteToHex(SUPds), 16);
				BigInteger remainder2 = base2.modPow(PROexponent, PROmodulus);
				String decryptSUPds = byteToHex(remainder2.toByteArray());
				decryptSUPds = decryptSUPds.substring(decryptSUPds.length() - 40, decryptSUPds.length());
				String hashSUPinfo = SHA(SUPinfo);
				if (decryptSUPds.equals(hashSUPinfo)) supplyVerificationLabel.setText("Correct");
				else supplyVerificationLabel.setText("Incorrect");
				
				// PART 3: Display d'informaci� en cas que tot sigui correcte:
				if (decryptPROds.equals(hashPROpub) && decryptSUPds.equals(hashSUPinfo)) {
					String nameColor;			
					switch (new String(color)) {
					case "Lc": nameColor = " (Light Cyan)"; 	break;
					case "Mk": nameColor = " (Matte Black)"; 	break;
					case " C": nameColor = " (Cyan)"; 			break;
					case "OP": nameColor = " (Optimizer)"; 		break;
					default  : nameColor = " Error";			break;
					}	
					partNumberLabel.setText(new String(number));
					selectabilityLabel.setText("HP " + new String(selectability));
					colorLabel.setText(new String(color) + nameColor);
					manufacturingDateLabel.setText(new String(year) + "/" + new String(month) + "/" + new String(day));
					manufacturingTimeLabel.setText(new String(hour) + ":" + new String(minute));
					writeStatusLabel.setText("");
				}
				
			} catch (STException e) {
			}
		}
	}
	private void updateWriteStatus(boolean success) {
		if (success) {
			writeStatusLabel.setText("Write successful");
		} else {
			writeStatusLabel.setText("Write failed");
		}
	}
	private boolean writeToTag() {
		if (recognizedNFCTag != null) {
			try {
				String data = dataArea.getText();
				byte [] dataToWrite;
				if (tipusData.equals("Hexadecimal")) dataToWrite = new BigInteger(cleanHex(data), 16).toByteArray();
				else if (tipusData.equals("Binary")) dataToWrite = new BigInteger(cleanBin(data), 2).toByteArray();
				else if (tipusData.equals("ASCII")) dataToWrite = data.getBytes();
				else return false;
				int address = 0x00;
				recognizedNFCTag.writeBytes(address, dataToWrite);
			} catch (STException e) {
				return false;
			}
			return true;
		}
		return false;
	}
	public static String cleanHex(String data) {
		int dataL = data.length();
		for (int i = dataL - 1; i >= 0; -- i) {
			int k = (int) data.charAt(i);
			boolean hex = ((k >= 48) && (k <= 57)) || ((k >= 65) && (k <= 70));
			if (! hex) data = removeChar(data, i);
		}
		return data;
	}
	public static String cleanBin(String data) {
		int dataL = data.length();
		for (int i = dataL - 1; i >= 0; -- i) {
			int k = (int) data.charAt(i);
			boolean bin = ((k == 48) || (k == 49));
			if (! bin) data = removeChar(data, i);
		}
		return data;
	}
	public static String removeChar(String word, int position) {
		return word.substring(0, position) + word.substring(position + 1, word.length());
	}
	public static String byteToHex(byte[] data) { 
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
	    return byteToHex(md.digest(convertme));
	}
	public static byte HPexp [] = {37};
	public static byte HPmod [] =
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
}