Feature:Satin alma sureci
  Scenario Outline:Belirli fiyat araligindeki urunun en düsük puanli saticidan sepete eklenmesi
    Given "<tarayici>" uzerinde "<url>" acilir
    When "<username>" ve "<password>" ile giris yapilir
    When "<urun>" isimli urun aranir
    When Fiyat araligi "<min>" ve "<max>" olarak secilir
    When En alttan rastgele urun secilir
    Then En dusuk puanli saticidan urun sepete eklenir

    Examples:
      | tarayici | url                          |  | username             | password | urun         | min  | max  |
      | Chrome   | https://www.hepsiburada.com/ |  | 2022testhb@gmail.com | Test2022 | cep telefonu | 3000 | 5000 |







