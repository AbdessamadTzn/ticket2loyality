import 'package:flutter/material.dart';

class ProfilePage extends StatelessWidget {
  const ProfilePage({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('User Profile'),
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          children: [
            Text(
              'User Profile', 
              style: Theme.of(context).textTheme.headlineMedium, // Remplace headline5 par headlineMedium
            ),
            const SizedBox(height: 20),
            // Autres éléments de la page...
          ],
        ),
      ),
    );
  }
}
