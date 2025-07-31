package main

import (
	"crypto/aes"
	"crypto/cipher"
	"crypto/rand"
	"crypto/sha256"
	"encoding/base64"
	"fmt"

	"golang.org/x/crypto/pbkdf2"
)

const (
	ITERATION_COUNT    = 19052004
	SALT_SIZE_BYTES    = 16
	IV_SIZE_BYTES      = 12
	AES_KEY_SIZE_BYTES = 32 // 256 bits
)

func encrypt(plaintext string, password string) (string, error) {

	// 1. Generate a random salt
	salt := make([]byte, SALT_SIZE_BYTES)
	if _, err := rand.Read(salt); err != nil {
		return "", fmt.Errorf("failed to generate salt: %w", err)
	}

	// 2. Derive the key using PBKDF2
	key := pbkdf2.Key([]byte(password), salt, ITERATION_COUNT, AES_KEY_SIZE_BYTES, sha256.New)

	// 3. Generate a random IV
	iv := make([]byte, IV_SIZE_BYTES)
	if _, err := rand.Read(iv); err != nil {
		return "", fmt.Errorf("failed to generate IV: %w", err)
	}

	// 4. Create the AES cipher block
	block, err := aes.NewCipher(key)
	if err != nil {
		return "", fmt.Errorf("failed to create cipher: %w", err)
	}

	// 5. Create GCM mode
	gcm, err := cipher.NewGCM(block)
	if err != nil {
		return "", fmt.Errorf("failed to create GCM: %w", err)
	}

	// 6. Encrypt and authenticate the data
	ciphertext := gcm.Seal(nil, iv, []byte(plaintext), nil)

	// 7. Combine salt, IV, and ciphertext into one payload
	payload := append(salt, iv...)
	payload = append(payload, ciphertext...)

	// 8. Encode the payload in base64
	return base64.StdEncoding.EncodeToString(payload), nil
}

func decrypt(base64Payload string, password string) (string, error) {

	decodedPayload, err := base64.StdEncoding.DecodeString(base64Payload)
	if err != nil {
		return "", fmt.Errorf("failed to decode base64: %w", err)
	}

	// 2. Extract salt, IV, and ciphertext from the combined payload
	if len(decodedPayload) < SALT_SIZE_BYTES+IV_SIZE_BYTES {
		return "", fmt.Errorf("payload is too short")
	}
	salt := decodedPayload[:SALT_SIZE_BYTES]
	iv := decodedPayload[SALT_SIZE_BYTES : SALT_SIZE_BYTES+IV_SIZE_BYTES]
	ciphertext := decodedPayload[SALT_SIZE_BYTES+IV_SIZE_BYTES:]

	// 3. Re-derive the key using PBKDF2 to match the Java implementation
	key := pbkdf2.Key([]byte(password), salt, ITERATION_COUNT, AES_KEY_SIZE_BYTES, sha256.New)

	// 4. Create the AES cipher block
	block, err := aes.NewCipher(key)
	if err != nil {
		return "", fmt.Errorf("failed to create cipher: %w", err)
	}

	// 5. Create GCM mode
	gcm, err := cipher.NewGCM(block)
	if err != nil {
		return "", fmt.Errorf("failed to create GCM: %w", err)
	}

	// 6. Decrypt and authenticate the data
	plaintext, err := gcm.Open(nil, iv, ciphertext, nil)
	if err != nil {
		// This is where the "message authentication failed" error occurs
		return "", fmt.Errorf("failed to decrypt: %w", err)
	}

	return string(plaintext), nil
}
func main() {
	// O token criptografado que você obteve do Python
	encryptedToken := "eaViwLOf5srpRZJSXgC4mdugj+RLpbi/R6h+AlFiQrTS6q+kyAc+7Wi7jHEDTcj9PKJXe9MTyrZJ8tPKO69Kc3SEkLPzPEW2Ypfh8atSN+e+E1hzEqSYPw4NaDXkW+2eWsrsd5tuBlDv+LflaWJ7yXSvIB/s5T0YNXLit7t3XcSZL8yf7n06JJ2iviCAyvplrIXbh+ckTcKnbniutuGK4xp6VlWh9W8xCSPrCabQE7nkxX97EULV/sntWFDTVw=="

	password := "rafinha19"

	decryptedToken, err := decrypt(encryptedToken, password)
	if err != nil {
		fmt.Println("Error decrypting token:", err)
		return
	}
	fmt.Println("Decrypted token:", decryptedToken)

}
