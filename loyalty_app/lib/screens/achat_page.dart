import 'package:flutter/material.dart';

class AchatPage extends StatelessWidget {
  const AchatPage({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Make a Purchase')),
      body: Center(
        child: ElevatedButton(
          onPressed: () {},
          child: const Text('Scan Receipt'),
        ),
      ),
    );
  }
}
