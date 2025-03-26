import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(home: ReceiptsScreen());
  }
}

class ReceiptsScreen extends StatefulWidget {
  @override
  _ReceiptsScreenState createState() => _ReceiptsScreenState();
}

class _ReceiptsScreenState extends State<ReceiptsScreen> {
  // Liste des tickets
  final List<Map<String, String>> receipts = [
    {
      'id': '1',
      'store': 'Supermarché ABC',
      'amount': '100,00 €',
      'price': '50,00 €',
      'quantity': '2',
    },
    {
      'id': '2',
      'store': 'Magasin XYZ',
      'amount': '80,00 €',
      'price': '40,00 €',
      'quantity': '2',
    },
    {
      'id': '3',
      'store': 'Boulangerie PQR',
      'amount': '25,00 €',
      'price': '25,00 €',
      'quantity': '1',
    },
  ];

  void handleRemoveReceipt(String id) {
    setState(() {
      receipts.removeWhere((receipt) => receipt['id'] == id);
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.blue[50], // Dégradé similaire à celui dans HTML
      body: Center(
        child: Container(
          width: 400,
          padding: EdgeInsets.all(30),
          decoration: BoxDecoration(
            color: Colors.white,
            borderRadius: BorderRadius.circular(12),
            boxShadow: [
              BoxShadow(
                color: Colors.black.withOpacity(0.1),
                spreadRadius: 4,
                blurRadius: 8,
                offset: Offset(0, 4),
              ),
            ],
          ),
          child: Column(
            mainAxisSize: MainAxisSize.min,
            children: [
              Text(
                'Mes Tickets',
                style: TextStyle(
                  fontSize: 24,
                  color: Colors.blue[800],
                  fontWeight: FontWeight.bold,
                ),
                textAlign:
                    TextAlign.center, // Le textAlign va ici dans le widget Text
              ),
              SizedBox(height: 20),
              receipts.isEmpty
                  ? Text(
                    'Aucun ticket disponible',
                    style: TextStyle(fontSize: 18, color: Colors.grey),
                  )
                  : Column(
                    children:
                        receipts.map((receipt) {
                          return Container(
                            margin: EdgeInsets.only(bottom: 10),
                            child: Column(
                              crossAxisAlignment: CrossAxisAlignment.start,
                              children: [
                                Text(
                                  receipt['store']!,
                                  style: TextStyle(
                                    fontSize: 18,
                                    fontWeight: FontWeight.bold,
                                    color: Colors.blue[800],
                                  ),
                                ),
                                Text('Montant Total: ${receipt['amount']}'),
                                Text('Prix Unitaire: ${receipt['price']}'),
                                Text('Quantité: ${receipt['quantity']}'),
                                ElevatedButton(
                                  style: ElevatedButton.styleFrom(
                                    backgroundColor: Colors.blue[600],
                                    foregroundColor: Colors.white,
                                    padding: EdgeInsets.all(15),
                                    shape: RoundedRectangleBorder(
                                      borderRadius: BorderRadius.circular(8),
                                    ),
                                  ),
                                  onPressed: () {
                                    handleRemoveReceipt(receipt['id']!);
                                  },
                                  child: Text(
                                    'Supprimer',
                                    style: TextStyle(
                                      fontWeight: FontWeight.bold,
                                    ),
                                  ),
                                ),
                              ],
                            ),
                          );
                        }).toList(),
                  ),
            ],
          ),
        ),
      ),
    );
  }
}
