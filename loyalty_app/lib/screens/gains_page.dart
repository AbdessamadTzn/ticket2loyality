import 'package:flutter/material.dart';

class GainsPage extends StatelessWidget {
  const GainsPage({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('My Gains')),
      body: Center(
        child: Text('Total Rewards: 120€'),
      ),
    );
  }
}
