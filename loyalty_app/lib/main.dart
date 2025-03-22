import 'package:flutter/material.dart';
import 'screens/home_page.dart';
import 'screens/login_page.dart';
import 'screens/register_page.dart';
import 'screens/profile_page.dart';
import 'screens/brands_page.dart';
import 'screens/gains_page.dart';
import 'screens/receipts_page.dart';
import 'screens/achat_page.dart';
import 'screens/phone_screen.dart'; // Ajout de l'import pour le phone_screen

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Loyalty App',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.deepPurple),
      ),
      home: const PhoneScreen(), // Changez ici pour afficher le PhoneScreen en page principale
      routes: {
        '/login': (context) => const LoginPage(),
        '/register': (context) => const RegisterPage(),
        '/profile': (context) => const ProfilePage(),
        '/brands': (context) => const BrandsPage(),
        '/gains': (context) => const GainsPage(),
        '/receipts': (context) => const ReceiptsPage(),
        '/achat': (context) => const AchatPage(),
      },
    );
  }
}
