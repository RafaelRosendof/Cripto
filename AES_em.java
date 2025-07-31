import java.util.ArrayList;
import java.util.List;

import javax.crypto.Cipher;
import javax.crypto.KeyGenerator;
import javax.crypto.SecretKey;
import javax.crypto.SecretKeyFactory;
import javax.crypto.spec.GCMParameterSpec;
import javax.crypto.spec.IvParameterSpec;
import javax.crypto.spec.PBEKeySpec;
import javax.crypto.spec.SecretKeySpec;

import java.nio.ByteBuffer;
import java.nio.charset.StandardCharsets;
import java.security.SecureRandom;
import java.security.spec.KeySpec;
import java.util.Base64;

public class AES_em {


    private static final int ITERATION_COUNT = 19052004;

    // Standard security parameters
    private static final String ENCRYPTION_ALGORITHM = "AES/GCM/NoPadding";
    private static final String KDF_ALGORITHM = "PBKDF2WithHmacSHA256";
    private static final int AES_KEY_SIZE_BITS = 256;
    private static final int GCM_IV_SIZE_BYTES = 12;
    private static final int GCM_TAG_SIZE_BITS = 128;
    private static final int SALT_SIZE_BYTES = 16;

    public static String encrypt(String plaintext, String password) throws Exception {
        // 1. A random salt and IV are generated. This is required for security.
        SecureRandom random = new SecureRandom();
        byte[] salt = new byte[SALT_SIZE_BYTES];
        random.nextBytes(salt);
        byte[] iv = new byte[GCM_IV_SIZE_BYTES];
        random.nextBytes(iv);

        // 2. The key is derived using the random salt and YOUR iteration count.
        SecretKeyFactory factory = SecretKeyFactory.getInstance(KDF_ALGORITHM);
        KeySpec spec = new PBEKeySpec(password.toCharArray(), salt, ITERATION_COUNT, AES_KEY_SIZE_BITS);
        SecretKey secretKey = new SecretKeySpec(factory.generateSecret(spec).getEncoded(), "AES");

        // 3. The data is encrypted.
        Cipher cipher = Cipher.getInstance(ENCRYPTION_ALGORITHM);
        GCMParameterSpec gcmParameterSpec = new GCMParameterSpec(GCM_TAG_SIZE_BITS, iv);
        cipher.init(Cipher.ENCRYPT_MODE, secretKey, gcmParameterSpec);
        byte[] ciphertext = cipher.doFinal(plaintext.getBytes(StandardCharsets.UTF_8));

        // 4. The salt, IV, and ciphertext are combined into a single package.
        ByteBuffer byteBuffer = ByteBuffer.allocate(salt.length + iv.length + ciphertext.length);
        byteBuffer.put(salt);
        byteBuffer.put(iv);
        byteBuffer.put(ciphertext);
        
        // 5. The final package is returned as a single string for storage.
        return Base64.getEncoder().encodeToString(byteBuffer.array());
    }

    public static String decrypt(String combinedData, String password) throws Exception {
        byte[] decodedPayload = Base64.getDecoder().decode(combinedData);
        ByteBuffer byteBuffer = ByteBuffer.wrap(decodedPayload);

        byte[] salt = new byte[SALT_SIZE_BYTES];
        byteBuffer.get(salt);
        byte[] iv = new byte[GCM_IV_SIZE_BYTES];
        byteBuffer.get(iv);
        byte[] ciphertext = new byte[byteBuffer.remaining()];
        byteBuffer.get(ciphertext);

        SecretKeyFactory factory = SecretKeyFactory.getInstance(KDF_ALGORITHM);
        KeySpec spec = new PBEKeySpec(password.toCharArray(), salt, ITERATION_COUNT, AES_KEY_SIZE_BITS);
        SecretKey secretKey = new SecretKeySpec(factory.generateSecret(spec).getEncoded(), "AES");

        Cipher cipher = Cipher.getInstance(ENCRYPTION_ALGORITHM);
        GCMParameterSpec gcmParameterSpec = new GCMParameterSpec(GCM_TAG_SIZE_BITS, iv);
        cipher.init(Cipher.DECRYPT_MODE, secretKey, gcmParameterSpec);
        byte[] decryptedText = cipher.doFinal(ciphertext);

        return new String(decryptedText, StandardCharsets.UTF_8);
    }
    
    public static void main(String[] args){

        String senha = "rafinha19";

        ArrayList<String> chaves = new ArrayList<>(java.util.Arrays.asList(
            "lady", "beef", "pudding", "bunker", "maze", "stumble", "rule", "neglect", "entry", "crime", "fun", "car", "avoid", "liquid", "roast", "puzzle", "cushion", "gate", "remember", "fun", "derive", "fall", "diagram", "nurse"
        ));
        

        try {
            String encrypted = encrypt("year work city bread fan genuine alley giggle wall jaguar easily stage shield fence toward enable length horn term battle badge inject gather fine" , "rafinha19");
            System.out.println("Encrypted: " + encrypted);
            String decrypted = decrypt(encrypted, "rafinha19");
            System.out.println("Decrypted: " + decrypted);
        } catch (Exception e) {
            e.printStackTrace();
        }

        
    }
} 