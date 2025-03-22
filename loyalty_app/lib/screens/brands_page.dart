import 'package:flutter/material.dart';

class BrandsPage extends StatefulWidget {
  const BrandsPage({Key? key}) : super(key: key);

  @override
  _BrandsPageState createState() => _BrandsPageState();
}

class _BrandsPageState extends State<BrandsPage> {
  // Liste de marques simulées (données fictives)
  List<Map<String, dynamic>> _brands = [
    {'brand_name': 'Brand A', 'rewards': 10},
    {'brand_name': 'Brand B', 'rewards': 15},
    {'brand_name': 'Brand C', 'rewards': 20},
    {'brand_name': 'Brand D', 'rewards': 30},
    {'brand_name': 'Brand E', 'rewards': 25},
  ];

  @override
  void initState() {
    super.initState();
    // Remarque : Nous n'avons plus besoin de la méthode _getBrands() pour récupérer les données.
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Brands')),
      body: _brands.isEmpty
          ? const Center(child: CircularProgressIndicator())
          : ListView.builder(
              itemCount: _brands.length,
              itemBuilder: (context, index) {
                var brand = _brands[index];
                return ListTile(
                  title: Text(brand['brand_name']),
                  subtitle: Text('Rewards: ${brand['rewards']}€'),
                  leading: const Icon(Icons.star),
                );
              },
            ),
    );
  }
}