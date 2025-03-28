import React, { useEffect, useState } from 'react';
import {
  View,
  Text,
  StyleSheet,
  ScrollView,
  TouchableOpacity,
  Image,
  ActivityIndicator,
} from 'react-native';
import { Ionicons } from '@expo/vector-icons';
import axios from 'axios';
import { router } from 'expo-router';

// URL de l'API backend
const API_URL = 'http://192.168.152.103:8000/api';

interface BrandStats {
  nom_marque: string;
  points: number;
  total_spent: number;
  total_tickets: number;
  total_items: number;
}

export default function GainsPage() {
  const [brandStats, setBrandStats] = useState<BrandStats[]>([]);
  const [loading, setLoading] = useState(true);
  const [totalPoints, setTotalPoints] = useState(0);

  const navigateToBrands = () => {
    router.push('/brands');
  };

  useEffect(() => {
    // Pour la démo, on utilise l'ID utilisateur 1
    fetchBrandStats(1);
  }, []);

  const fetchBrandStats = async (userId: number) => {
    try {
      const response = await axios.get(`${API_URL}/user/${userId}/brand-stats`);
      setBrandStats(response.data);
      // Calculer le total des points
      const total = response.data.reduce(
        (acc: number, curr: BrandStats) => acc + curr.points,
        0
      );
      setTotalPoints(total);
    } catch (error) {
      console.error('Erreur lors de la récupération des statistiques:', error);
    } finally {
      setLoading(false);
    }
  };

  const getProgressColor = (points: number) => {
    if (points >= 100) return '#4CAF50';
    if (points >= 50) return '#2196F3';
    if (points >= 25) return '#FFC107';
    return '#FF5722';
  };

  return (
    <View style={styles.container}>
      <View style={styles.header}>
        <Text style={styles.title}>Mes Gains</Text>
        <View style={styles.totalPointsContainer}>
          <Text style={styles.totalPointsLabel}>Total des gains</Text>
          <Text style={styles.totalPointsValue}>{totalPoints}€</Text>
        </View>
      </View>

      <ScrollView style={styles.scrollView}>
        {loading ? (
          <View style={styles.loadingContainer}>
            <ActivityIndicator size="large" color="#2196F3" />
            <Text style={styles.loadingText}>Chargement de vos gains...</Text>
          </View>
        ) : brandStats.length === 0 ? (
          <View style={styles.noDataContainer}>
            <Ionicons name="receipt-outline" size={64} color="#666" />
            <Text style={styles.noDataText}>
              Scannez vos tickets pour commencer à gagner des points!
            </Text>
          </View>
        ) : (
          brandStats.map((brand, index) => (
            <TouchableOpacity key={index} style={styles.brandCard}>
              <View style={styles.brandHeader}>
                <Text style={styles.brandName}>{brand.nom_marque}</Text>
                <View style={styles.statsContainer}>
                  <View style={styles.statItem}>
                    <Ionicons name="receipt-outline" size={16} color="#666" />
                    <Text style={styles.statText}>
                      {brand.total_tickets} tickets
                    </Text>
                  </View>
                  <View style={styles.statItem}>
                    <Ionicons name="cart-outline" size={16} color="#666" />
                    <Text style={styles.statText}>
                      {brand.total_items} articles
                    </Text>
                  </View>
                </View>
              </View>

              <View style={styles.pointsSection}>
                <View style={styles.pointsInfo}>
                  <Text style={styles.pointsValue}>{brand.points}€</Text>
                  <Text style={styles.pointsLabel}>économisés</Text>
                </View>
                <View style={styles.progressContainer}>
                  <View style={styles.progressBar}>
                    <View
                      style={[
                        styles.progressFill,
                        {
                          width: `${Math.min(
                            (brand.points / 100) * 100,
                            100
                          )}%`,
                          backgroundColor: getProgressColor(brand.points),
                        },
                      ]}
                    />
                  </View>
                  <Text style={styles.progressText}>
                    {brand.points < 100
                      ? `${100 - brand.points}€ pour le prochain palier`
                      : 'Palier atteint !'}
                  </Text>
                </View>
              </View>

              <TouchableOpacity
                style={[
                  styles.viewButton,
                  { backgroundColor: getProgressColor(brand.points) },
                ]}
              >
                <Text style={styles.viewButtonText}>Voir le détail</Text>
                <Ionicons name="chevron-forward" size={20} color="#FFF" />
              </TouchableOpacity>
            </TouchableOpacity>
          ))
        )}
      </ScrollView>

      {/* Barre de navigation */}
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
        <TouchableOpacity style={styles.navItem} onPress={navigateToBrands}>
          <Ionicons name="business" size={24} color="#666" />
        </TouchableOpacity>
        <TouchableOpacity style={styles.navItem}>
          <Ionicons name="trophy" size={24} color="#2196F3" />
        </TouchableOpacity>
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#f5f5f5',
  },
  header: {
    padding: 20,
    paddingTop: 60,
    backgroundColor: '#fff',
    borderBottomWidth: 1,
    borderBottomColor: '#e0e0e0',
  },
  title: {
    fontSize: 28,
    fontWeight: 'bold',
    marginBottom: 10,
  },
  totalPointsContainer: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
  },
  totalPointsLabel: {
    fontSize: 16,
    color: '#666',
  },
  totalPointsValue: {
    fontSize: 24,
    fontWeight: 'bold',
    color: '#2196F3',
  },
  scrollView: {
    flex: 1,
  },
  loadingContainer: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    padding: 20,
  },
  loadingText: {
    marginTop: 10,
    fontSize: 16,
    color: '#666',
  },
  noDataContainer: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    padding: 20,
  },
  noDataText: {
    marginTop: 10,
    fontSize: 16,
    color: '#666',
    textAlign: 'center',
  },
  brandCard: {
    margin: 10,
    padding: 15,
    backgroundColor: '#fff',
    borderRadius: 12,
    elevation: 2,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.1,
    shadowRadius: 4,
  },
  brandHeader: {
    marginBottom: 15,
  },
  brandName: {
    fontSize: 20,
    fontWeight: 'bold',
    marginBottom: 8,
  },
  statsContainer: {
    flexDirection: 'row',
    gap: 15,
  },
  statItem: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 5,
  },
  statText: {
    fontSize: 14,
    color: '#666',
  },
  pointsSection: {
    flexDirection: 'row',
    alignItems: 'center',
    marginBottom: 15,
  },
  pointsInfo: {
    width: 100,
  },
  pointsValue: {
    fontSize: 24,
    fontWeight: 'bold',
    color: '#2196F3',
  },
  pointsLabel: {
    fontSize: 12,
    color: '#666',
  },
  progressContainer: {
    flex: 1,
  },
  progressBar: {
    height: 8,
    backgroundColor: '#e0e0e0',
    borderRadius: 4,
    marginBottom: 5,
  },
  progressFill: {
    height: '100%',
    borderRadius: 4,
  },
  progressText: {
    fontSize: 12,
    color: '#666',
  },
  viewButton: {
    flexDirection: 'row',
    justifyContent: 'center',
    alignItems: 'center',
    padding: 12,
    borderRadius: 8,
    gap: 5,
  },
  viewButtonText: {
    color: '#fff',
    fontSize: 16,
    fontWeight: '500',
  },
  bottomNav: {
    flexDirection: 'row',
    justifyContent: 'space-around',
    alignItems: 'center',
    height: 60,
    backgroundColor: '#fff',
    borderTopWidth: 1,
    borderTopColor: '#e0e0e0',
    paddingBottom: 20,
  },
  navItem: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
  },
  scanButton: {
    width: 56,
    height: 56,
    borderRadius: 28,
    backgroundColor: '#2196F3',
    justifyContent: 'center',
    alignItems: 'center',
    marginBottom: 28,
  },
  scanButtonInner: {
    width: 52,
    height: 52,
    borderRadius: 26,
    backgroundColor: '#2196F3',
    justifyContent: 'center',
    alignItems: 'center',
    borderWidth: 3,
    borderColor: '#fff',
  },
});
