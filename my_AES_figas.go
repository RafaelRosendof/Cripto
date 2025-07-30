package main

import (
	"encoding/base64"
	"fmt"
	"time"

	"github.com/fernet/fernet-go"
)

func gerarChaveCustomizada(senha string) string {
	keyBytes := []byte(senha)
	keyLen := len(keyBytes)

	if keyLen < 32 {
		// Se a senha for menor que 32, preenche com espaços à direita.
		padding := make([]byte, 32-keyLen)
		for i := range padding {
			padding[i] = ' ' // O caractere de espaço
		}
		keyBytes = append(keyBytes, padding...)
	} else if keyLen > 32 {
		// Se for maior, corta em 32.
		keyBytes = keyBytes[:32]
	}

	// Codifica os 32 bytes resultantes para Base64 URL-safe, como no Python.
	return base64.URLEncoding.EncodeToString(keyBytes)
}

func main() {
	// O token criptografado que você obteve do Python
	encryptedToken := "gAAAAABoiThtWaC3it-pIj2ULDI_E7oWXre6Z8D8MV3RNPrVOQVUgrfutRCBy1SX0I2EbUHq_MSUHViWhkimxBebd5r0Kgn9rmut_PpgtmFVO9hFCkxjLOkay0iA8U1dVtYQtPvMGHBD7Nn42vrIIA6mSSH6A9lgjfQTVt8i66E5MdXWjF0OT_-33tCNBP3dK6_opHU_cQR3-tJze7kz4Gqvq32HEVPGyHaW9FRA7XxF9CtgZCoKTzjZEvox6PTyWOcQqXvAjHpVpkSfLqEwDlxQkJr-4PCaIw=="

	// A senha original
	password := "rafinha19"

	// 1. Gera a chave usando a mesma lógica customizada do Python
	keyString := gerarChaveCustomizada(password)

	// fmt.Printf("Chave Gerada: %s\n", keyString) // Descomente para ver a chave

	// 2. Decodifica a chave Base64 para usar com a biblioteca Fernet
	keys := fernet.MustDecodeKeys(keyString)

	// 3. Tenta descriptografar a mensagem usando a chave correta
	decryptedMsg := fernet.VerifyAndDecrypt([]byte(encryptedToken), 365*24*time.Hour, keys)

	if decryptedMsg == nil {
		fmt.Println("Erro: Falha ao verificar ou descriptografar o token. A chave pode estar errada ou o token corrompido.")
	} else {
		fmt.Println("SUCESSO!")
		fmt.Printf("Texto original: %s\n", decryptedMsg)
	}
}
