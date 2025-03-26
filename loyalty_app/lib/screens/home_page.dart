import 'package:flutter/material.dart';
import 'brands_page.dart';
import 'gains_page.dart';
import 'receipts_page.dart';
import 'profile_page.dart';

class HomePage extends StatefulWidget {
  const HomePage({super.key});

  @override
  _HomePageState createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  int _selectedIndex = 0;

  // Liste des pages associées aux onglets
  final List<Widget> _pages = [
    BrandsPage(), // Marques
    GainsPage(), // Gains
    ReceiptsScreen(), // Tickets
    UserProfile(), // Profil
  ];

  void _onItemTapped(int index) {
    setState(() {
      _selectedIndex = index;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: _pages[_selectedIndex], // Affichage de la page sélectionnée
      bottomNavigationBar: BottomAppBar(
        shape: const CircularNotchedRectangle(),
        notchMargin: 8.0,
        child: Row(
          mainAxisAlignment: MainAxisAlignment.spaceAround,
          children: <Widget>[
            IconButton(
              icon: const Icon(Icons.store),
              color: _selectedIndex == 0 ? Colors.deepPurple : Colors.grey,
              onPressed: () => _onItemTapped(0),
            ),
            IconButton(
              icon: const Icon(Icons.emoji_events),
              color: _selectedIndex == 1 ? Colors.deepPurple : Colors.grey,
              onPressed: () => _onItemTapped(1),
            ),
            const SizedBox(width: 40), // Espace pour le bouton flottant
            IconButton(
              icon: const Icon(Icons.receipt_long),
              color: _selectedIndex == 2 ? Colors.deepPurple : Colors.grey,
              onPressed: () => _onItemTapped(2),
            ),
            IconButton(
              icon: const Icon(Icons.person),
              color: _selectedIndex == 3 ? Colors.deepPurple : Colors.grey,
              onPressed: () => _onItemTapped(3),
            ),
          ],
        ),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: () => Navigator.pushNamed(context, '/scan'),
        backgroundColor: Colors.deepPurple,
        child: const Icon(Icons.qr_code_scanner, size: 30, color: Colors.white),
      ),
      floatingActionButtonLocation: FloatingActionButtonLocation.centerDocked,
    );
  }
}
