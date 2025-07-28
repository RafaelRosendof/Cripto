package main

import (
	"fmt"
)

// Etapa 1: Operação matemática (adição modular)
// Adiciona os bytes da senha aos bytes dos dados, repetindo a senha se necessário.
func addKey(data []byte, key []byte) []byte {
	encrypted := make([]byte, len(data))
	for i := 0; i < len(data); i++ {
		// A adição de bytes em Go já faz o "wrap-around" (aritmética modular)
		encrypted[i] = data[i] + key[i%len(key)] // i % len(key) repete a chave
	}
	return encrypted
}

// Etapa 2: Shift (rotação circular para a direita)
func shiftRight(data []byte) []byte {
	if len(data) == 0 {
		return data
	}
	// Salva o último elemento
	last := data[len(data)-1]
	// Move todos os elementos uma posição para a direita
	copy(data[1:], data[:len(data)-1])
	// Coloca o último elemento no início
	data[0] = last
	return data
}

func main() {
	words := []string{"year", "toy", "apple"}
	password := "figas"

	// Converte a senha para bytes uma vez
	keyBytes := []byte(password)

	fmt.Printf("Senha: %s -> Bytes: %v\n\n", password, keyBytes)

	for _, word := range words {
		fmt.Printf("--- Processando Palavra: %s ---\n", word)
		
		// Converte a palavra para bytes
		dataBytes := []byte(word)
		fmt.Printf("Original:\t%s -> %v\n", word, dataBytes)

		// Etapa 1: Adicionar a chave
		added := addKey(dataBytes, keyBytes)
		fmt.Printf("Após Adição:\t%v\n", added)

		// Etapa 2: Fazer o shift
		shifted := shiftRight(added)
		fmt.Printf("Após Shift:\t%v -> %s (tentativa de decodificar)\n\n", shifted, string(shifted))
	}
}
