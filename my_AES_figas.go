package main

import (
	"crypto/aes"
	"crypto/cipher"
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

func decrypt(base64Payload string, password string) (string, error) {
	// 1. Decode the Base64 payload
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
	encryptedToken := "ulqPPpqKNjh1bOBm8fz8aSdNLje3yG58v6wLGcJdKYpBHwftMnGpDhHnPfptzVoaGLF0zUdgcHO93FnS1FnSKCA15RCfwDKwKKLOap+Z9JxBdnTH9ERT2rNPzLKJtc+Ry1RVi4NS2ZNGMiem9DX/TvfwVaxkXRX/hO31V0+DRxhLcuFdIUJnuAvrrfls+f2LcPi9brg72ikh/a+c8bTIlDdfj5euvg66dmxolxSVVadEHVjXTF4jqUHzllHh5A=="

	password := "rafinha19"

	decryptedToken, err := decrypt(encryptedToken, password)
	if err != nil {
		fmt.Println("Error decrypting token:", err)
		return
	}
	fmt.Println("Decrypted token:", decryptedToken)

}
