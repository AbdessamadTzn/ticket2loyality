import {
  View,
  Text,
  StyleSheet,
  ScrollView,
  TouchableOpacity,
} from 'react-native';
import { Ionicons } from '@expo/vector-icons';
import { router } from 'expo-router';

const BRANDS = [
  { id: 1, name: 'Pringles' },
  { id: 2, name: 'Mango' },
  { id: 3, name: 'Puma' },
  { id: 4, name: 'Samsung' },
  { id: 5, name: 'Sodebo' },
  { id: 6, name: 'Candia' },
];

export default function BrandsPage() {
  const navigateToGains = () => {
    router.push('/gains');
  };

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

      <View style={styles.bottomNav}>
        <TouchableOpacity style={styles.navItem}>
          <Ionicons name="person-outline" size={24} color="#666" />
        </TouchableOpacity>
        <TouchableOpacity style={styles.navItem}>
          <Ionicons name="time-outline" size={24} color="#666" />
        </TouchableOpacity>
        <TouchableOpacity style={styles.scanButton}>
          <View style={styles.scanButtonInner}>
            <Ionicons name="scan" size={24} color="#FFF" />
          </View>
        </TouchableOpacity>
        <TouchableOpacity style={styles.navItem}>
          <Ionicons name="business" size={24} color="#2196F3" />
        </TouchableOpacity>
        <TouchableOpacity style={styles.navItem} onPress={navigateToGains}>
          <Ionicons name="trophy" size={24} color="#666" />
        </TouchableOpacity>
      </View>
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
  bottomNav: {
    flexDirection: 'row',
    height: 60,
    backgroundColor: '#fff',
    borderTopWidth: 1,
    borderTopColor: '#e0e0e0',
    justifyContent: 'space-around',
    alignItems: 'center',
  },
  navItem: {
    flex: 1,
    alignItems: 'center',
  },
  scanButton: {
    flex: 1,
    alignItems: 'center',
  },
  scanButtonInner: {
    width: 56,
    height: 56,
    borderRadius: 28,
    backgroundColor: '#2196F3',
    justifyContent: 'center',
    alignItems: 'center',
    marginBottom: 20,
  },
});
