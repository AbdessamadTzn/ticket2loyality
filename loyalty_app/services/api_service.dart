import 'dart:convert';
import 'package:http/http.dart' as http;

class ApiService {
  final String baseUrl = 'http://YOUR_API_URL';

  Future<List<Map<String, dynamic>>> getBrands() async {
    final response = await http.get(Uri.parse('$baseUrl/brands'));
    if (response.statusCode == 200) {
      List<dynamic> data = json.decode(response.body);
      return List<Map<String, dynamic>>.from(data);
    } else {
      throw Exception('Failed to load brands');
    }
  }
}
