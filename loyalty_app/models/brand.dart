class Brand {
  final String name;
  final double rewards;

  Brand({required this.name, required this.rewards});

  factory Brand.fromJson(Map<String, dynamic> json) {
    return Brand(
      name: json['name'],
      rewards: json['rewards'],
    );
  }
}
