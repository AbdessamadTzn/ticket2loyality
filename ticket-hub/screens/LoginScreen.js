import React, { useState } from 'react';
import { StyleSheet, View, Text } from 'react-native';
import { TextInput, Button } from 'react-native-paper';

export default function LoginScreen({ navigation }) {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleLogin = async () => {
    try {
      setLoading(true);
      setError('');

      // Pour la démo, on vérifie directement les credentials par défaut
      if (email === 'tickethub@gmail.com' && password === 'Test123') {
        navigation.replace('Brands');
      } else {
        setError('Email ou mot de passe incorrect');
      }
    } catch (err) {
      setError('Une erreur est survenue');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <View style={styles.container}>
      <View style={styles.header}>
        <Text style={styles.title}>Ticket Hub</Text>
        <Text style={styles.subtitle}>Scannez. Gagnez. Profitez.</Text>
      </View>

      <View style={styles.form}>
        <TextInput
          label="Email"
          value={email}
          onChangeText={setEmail}
          mode="outlined"
          style={styles.input}
          keyboardType="email-address"
          autoCapitalize="none"
        />

        <TextInput
          label="Mot de passe"
          value={password}
          onChangeText={setPassword}
          mode="outlined"
          style={styles.input}
          secureTextEntry
        />

        {error ? <Text style={styles.error}>{error}</Text> : null}

        <Button
          mode="contained"
          onPress={handleLogin}
          loading={loading}
          style={styles.button}
          disabled={loading}
        >
          Se connecter
        </Button>

        <Text style={styles.noAccountText}>
          Pas de compte ? Contactez votre administrateur
        </Text>
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    padding: 20,
  },
  header: {
    alignItems: 'center',
    marginTop: 100,
    marginBottom: 50,
  },
  title: {
    fontSize: 32,
    fontWeight: 'bold',
    color: '#000',
    marginBottom: 10,
  },
  subtitle: {
    fontSize: 16,
    color: '#666',
  },
  form: {
    flex: 1,
    justifyContent: 'center',
    marginBottom: 100,
  },
  input: {
    marginBottom: 15,
    backgroundColor: '#fff',
  },
  button: {
    marginTop: 10,
    paddingVertical: 8,
    backgroundColor: '#2196F3',
  },
  error: {
    color: 'red',
    marginBottom: 10,
    textAlign: 'center',
  },
  noAccountText: {
    marginTop: 20,
    textAlign: 'center',
    color: '#666',
  },
});
