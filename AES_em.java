import java.util.ArrayList;
import java.util.List;

import javax.crypto.Cipher;
import javax.crypto.KeyGenerator;
import javax.crypto.SecretKey;
import javax.crypto.spec.IvParameterSpec;
import javax.crypto.spec.SecretKeySpec;
import java.security.SecureRandom;
import java.util.Base64;

public class AES_em {


    //get the AES without using salt and other methods like that
    public static SecretKey encrypt(String senha) throws Exception {

        KeyGenerator keyGen = KeyGenerator.getInstance("AES");
        keyGen.init(256); 
        return keyGen.generateKey();
    }

    public static SecretKey getKeyFromPass(String plaintext, String senha) throws Exception {

    }

    
    public static void main(String[] args){

        String senha = "rafinha19";

        ArrayList<String> chaves = new ArrayList<>(java.util.Arrays.asList(
            "lady", "beef", "pudding", "bunker", "maze", "stumble", "rule", "neglect", "entry", "crime", "fun", "car", "avoid", "liquid", "roast", "puzzle", "cushion", "gate", "remember", "fun", "derive", "fall", "diagram", "nurse"
        ));
        

        
    }
} 