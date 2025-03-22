import 'package:flutter/material.dart';

class ReceiptsPage extends StatelessWidget {
  const ReceiptsPage({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Receipts')),
      body: ListView(
        children: <Widget>[
          ListTile(title: Text('Store: ABC Store, Amount: 26.99€')),
          ListTile(title: Text('Store: XYZ Store, Amount: 12.33€')),
        ],
      ),
    );
  }
}
