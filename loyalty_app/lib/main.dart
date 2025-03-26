import 'package:flutter/material.dart';
import 'screens/welcome_page.dart';
import 'screens/home_page.dart';
import 'screens/login_page.dart';
import 'screens/register_page.dart';
import 'screens/profile_page.dart';
import 'screens/brands_page.dart';
import 'screens/gains_page.dart';
import 'screens/receipts_page.dart';
import 'screens/achat_page.dart';
import 'screens/scan_page.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Loyalty App',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.deepPurple),
      ),
      home: WelcomePage(), // Retirer 'const'
      routes: {
        '/home': (context) => HomePage(), // Retirer 'const'
        '/login': (context) => LoginPage(), // Retirer 'const'
        '/register': (context) => RegisterPage(), // Retirer 'const'
        '/profile': (context) => UserProfile(), // Retirer 'const'
        '/brands': (context) => BrandsPage(), // Retirer 'const'
        '/gains': (context) => GainsPage(), // Retirer 'const'
        '/receipts': (context) => ReceiptsScreen(), // Retirer 'const'
        '/achat': (context) => AchatsPage(), // Retirer 'const'
        '/scan': (context) => ScanPage(), // Retirer 'const'
      },
    );
  }
}
