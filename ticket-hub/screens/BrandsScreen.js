import React from 'react';
import {
  View,
  Text,
  StyleSheet,
  ScrollView,
  TouchableOpacity,
} from 'react-native';
import BottomNavigation from '../components/BottomNavigation';

// Liste des marques (à remplacer par les données de l'API)
const BRANDS = [
  { id: 1, name: 'Pringles' },
  { id: 2, name: 'Mango' },
  { id: 3, name: 'Puma' },
  { id: 4, name: 'Samsung' },
  { id: 5, name: 'Sodebo' },
  { id: 6, name: 'Candia' },
];

export default function BrandsScreen({ navigation }) {
  return (
    <View style={styles.container}>
      <View style={styles.header}>
        <Text style={styles.title}>Nos marques partenaires</Text>
      </View>

      <ScrollView style={styles.scrollView}>
        <View style={styles.brandsGrid}>
          {BRANDS.map((brand) => (
            <TouchableOpacity
              key={brand.id}
              style={styles.brandItem}
              onPress={() => {
                /* Navigation vers les détails de la marque */
              }}
            >
              <View style={styles.brandBox}>
                <Text style={styles.brandName}>{brand.name}</Text>
              </View>
            </TouchableOpacity>
          ))}
        </View>
      </ScrollView>

      <BottomNavigation navigation={navigation} activeScreen="Brands" />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
  },
  header: {
    padding: 20,
    paddingTop: 60,
    backgroundColor: '#fff',
    borderBottomWidth: 1,
    borderBottomColor: '#e0e0e0',
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
  },
  scrollView: {
    flex: 1,
  },
  brandsGrid: {
    padding: 10,
    flexDirection: 'row',
    flexWrap: 'wrap',
    justifyContent: 'space-between',
  },
  brandItem: {
    width: '48%',
    marginBottom: 15,
  },
  brandBox: {
    backgroundColor: '#f5f5f5',
    padding: 20,
    borderRadius: 10,
    alignItems: 'center',
    justifyContent: 'center',
    height: 100,
  },
  brandName: {
    fontSize: 16,
    fontWeight: '500',
    textAlign: 'center',
  },
});
