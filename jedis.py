jedis = [
    {'nombre': 'Anakin', 'raza': 'Humano','planeta_origen': 'Tatooine', 'color_espada': 'Azul'},
    {'nombre': 'Primer Jedi', 'raza': 'Desconocido','planeta_origen': 'Ahch-To', 'color_espada': 'Desconocido'},
    {'nombre': 'Obi-Wan Kenobi', 'raza': 'Humano','planeta_origen':'Stewjon', 'color_espada': 'Azul'},
    {'nombre': 'Yarael Poof', 'raza': 'Quermiano','planeta_origen':'Quermia', 'color_espada': 'Azul'},
    {'nombre': 'Coleman Trebor', 'raza': 'Vurk','planeta_origen':'Sembla', 'color_espada': 'Verde'},
    {'nombre': 'Eno Cordova', 'raza': 'Humano','planeta_origen':'Desconocido', 'color_espada': 'Azul'},
    {'nombre': 'Cere Junda', 'raza': 'Humano','planeta_origen':'Desconocido', 'color_espada': 'Verde'},
    {'nombre': 'Cal Kestis', 'raza': 'Humano','planeta_origen':'Desconocido', 'color_espada': 'Variocolor Doble'},
    {'nombre': 'Trilla Suduri', 'raza': 'Humano','planeta_origen':'Desconocido', 'color_espada': 'Rojo'},
    {'nombre': 'Cyslin Myr', 'raza': 'Mirialano','planeta_origen':'Mirial', 'color_espada': 'Plata'},
    {'nombre': 'Rahm Kota', 'raza': 'Humano','planeta_origen':'Desconocido', 'color_espada': 'Verde'},
    {'nombre': 'Oppo Rancisis', 'raza': 'Thisspiasiano','planeta_origen':'Thisspias', 'color_espada': 'Verde'},
    {'nombre': 'Ima-Gun Di', 'raza': 'Nikto','planeta_origen':'Kintan', 'color_espada': 'Azul'},
    {'nombre': 'Poli Dapatian', 'raza': 'Humano','planeta_origen':'Desconocido', 'color_espada': 'Verde'},
    {'nombre': 'Ferren Barr', 'raza': 'Iktotchi','planeta_origen':'Iktotch', 'color_espada': 'Azul'},
    {'nombre': 'Kit Fisto', 'raza': 'Nautolano','planeta_origen':'Glee Anselm', 'color_espada': 'Verde'},
    {'nombre': 'Stass Allie', 'raza': 'Tholothiana','planeta_origen':'Tholoth', 'color_espada': 'Verde'},
    {'nombre': 'Ikrit', 'raza': 'kushibano','planeta_origen':'Kushiban', 'color_espada': 'Desconocido'},
    {'nombre': 'Zez-Kai_Ell', 'raza': 'Humano','planeta_origen':'Mandalor', 'color_espada': 'Morado Doble'},
    {'nombre': 'Saesee Tiin', 'raza': 'Iktotchi','planeta_origen':'Iktotch', 'color_espada': 'Verde'},
    {'nombre': 'Bastila Shan', 'raza': 'Humano','planeta_origen':'Talravin', 'color_espada': 'Amarillo Doble y Rojo Doble'},
    {'nombre': 'Tyvokka', 'raza': 'Wookiee','planeta_origen':'Kashyyk', 'color_espada': 'Amarillo'},
    {'nombre': 'Even Piell', 'raza': 'Lannik','planeta_origen':'Lannik','color_espada':'Verde'},
    {'nombre': 'Tiplee', 'raza': 'Mikkiano','planeta_origen':'Mikkia', 'color_espada': 'Verde'},
    {'nombre': 'Tiplar', 'raza': 'Mikkiano','planeta_origen':'Mikkia', 'color_espada': 'Azul'},
    {'nombre': 'Tu-Anh', 'raza': 'Humano','planeta_origen':'Desconocido', 'color_espada': 'Desconocido'},
    {'nombre': 'Tsui Choi', 'raza': 'Aleena','planeta_origen':'Aleen', 'color_espada': 'Verde'},
    {'nombre': 'Ronhar Kim', 'raza': 'Humano','planeta_origen':'Naboo', 'color_espada': 'Azul'},
    {'nombre': 'Plo Koon', 'raza': 'Kel Dor','planeta_origen':'Dorin', 'color_espada': 'Azul'},
    {'nombre': 'Ki-Adi-Mundi', 'raza': 'Cerean','planeta_origen':'Cerea', 'color_espada': 'Azul'},
    {'nombre': 'Eeth Koth', 'raza': 'Zabrak','planeta_origen':'Iridonia', 'color_espada': 'Verde'},
    {'nombre': 'Zao', 'raza': 'Veknoide','planeta_origen':'Veknor', 'color_espada': 'Azul'},
    {'nombre': 'Vrook Lamar', 'raza': 'Humano','planeta_origen':'Dantooine', 'color_espada': 'Verde'},
    {'nombre': 'Ooroo', 'raza': 'Celegiano','planeta_origen':'Celegia', 'color_espada': 'Desconocido'},
    {'nombre': 'Bao-Dur', 'raza': 'Zabrak','planeta_origen':'Iridonia', 'color_espada': 'Amarillo Doble'},
    {'nombre': 'Bolla Ropal', 'raza': 'Rodiano','planeta_origen':'Rodia', 'color_espada': 'Verde'},
    {'nombre': 'Agen Kolar', 'raza': 'Zabrak','planeta_origen':'Coruscan', 'color_espada': 'Azul'},
    {'nombre': 'Depa Billaba', 'raza': 'Humano','planeta_origen':'Chalacta', 'color_espada': 'Verde'},
    {'nombre': 'Luke Skywalker', 'raza': 'Humano','planeta_origen':'Tatooine', 'color_espada': 'Verde'},
    {'nombre': 'Aayla Secura', 'raza': 'Twi,lek','planeta_origen':'Ryloth', 'color_espada': 'Azul, Verde'},
    {'nombre': 'Sifo-Dyas', 'raza': 'Humano','planeta_origen':'Mundos Cassandranos', 'color_espada': 'Azul'},
    {'nombre': 'Dar,Nala', 'raza': 'Togruta','planeta_origen':'Shili', 'color_espada': 'Azul'},
    {'nombre': 'Jocasta Nu', 'raza': 'Humano','planeta_origen':'Coruscant', 'color_espada': 'Azul'},
    {'nombre': 'Aryn Leneer', 'raza': 'Humano','planeta_origen':'Balmorra', 'color_espada': 'Azul'},
    {'nombre': 'Bolook', 'raza': 'Twi,lek','planeta_origen':'Ryloth', 'color_espada': 'Rosa'},
    {'nombre': 'Brianna', 'raza': 'Humano','planeta_origen':'Desconocido', 'color_espada': 'Blanco'},
    {'nombre': 'Revan', 'raza': 'Humano','planeta_origen':'En algún lugar de los Territorios del Borde Exterior', 'color_espada': 'Morado y Rojo'},
    {'nombre': 'Ood Bnar', 'raza': 'Neti','planeta_origen':'Netidia', 'color_espada': 'Verde'},
    {'nombre': 'Jolee Bindo', 'raza': 'Humano','planeta_origen':'Kashyyyk', 'color_espada': 'Azul'},
    {'nombre': 'Dorjander Kace', 'raza': 'Humano','planeta_origen':'Mandalor', 'color_espada': 'Naranja'},
    {'nombre': 'Juhani', 'raza': 'Cátaro','planeta_origen':'Dantooine', 'color_espada': 'Azul'},
    {'nombre': 'Bela Kiwiiks', 'raza': 'Togruta','planeta_origen':'Shili', 'color_espada': 'Azul'},
    {'nombre': 'Syo Bakarn', 'raza': 'Humano','planeta_origen':'Tython', 'color_espada': 'Violeta'},
    {'nombre': 'Exar Kun', 'raza': 'Humano','planeta_origen':'Desconocido', 'color_espada': 'Azul Doble'},
    {'nombre': 'Jaro Tapal', 'raza': 'Lasat','planeta_origen':'Lasan', 'color_espada': 'Azul Doble'},
    {'nombre': 'Luminara Unduli', 'raza': 'Mirialan','planeta_origen':'Mirial', 'color_espada': 'Verde'},
    {'nombre': 'Barriss Offee', 'raza': 'Mirialan','planeta_origen':'Mirial', 'color_espada': 'Azul'},
    {'nombre': 'Shaak Ti', 'raza': 'Togruta','planeta_origen':'Shili', 'color_espada': 'Azul'},
    {'nombre': 'Bo-Katan Kryze', 'raza': 'Humano','planeta_origen':'Mandalor', 'color_espada': 'Negro'},
    {'nombre': 'Ahsoka Tano', 'raza': 'Togruta','planeta_origen':'Shili', 'color_espada': 'Verde y Azul, Blanco y Blanco'},
    {'nombre': 'Kanan Jarrus', 'raza': 'Humano','planeta_origen':'Coruscant', 'color_espada': 'Azul'},
    {'nombre': 'Ezra Bridger', 'raza': 'Humano','planeta_origen':'Lothal', 'color_espada': 'Verde'},
    {'nombre': 'Ben Solo', 'raza': 'Humano','planeta_origen':'Chandrila', 'color_espada': 'Verde, Rojo'},
    {'nombre': 'Rey Skywalker', 'raza': 'Humano','planeta_origen':'Jakku', 'color_espada': 'Amarillo, Verde, Azul'},
    {'nombre': 'Yoda', 'raza': 'La especie de Yoda','planeta_origen':'Dagobah', 'color_espada': 'Verde'},
    {'nombre': 'Leia Organa', 'raza': 'Humano','planeta_origen':'Alderaan', 'color_espada': 'Azul'},
    {'nombre': 'Dooku', 'raza': 'Humano','planeta_origen':'Serenno', 'color_espada': 'Azul, Rojo'},
    {'nombre': 'Maul', 'raza': 'Zabrak','planeta_origen':'Dathomir', 'color_espada': 'Rojo Doble'},
    {'nombre': 'Savage Opress', 'raza': 'Zabrak','planeta_origen':'Dathomir', 'color_espada': 'Rojo Doble'},
    {'nombre': 'Mace Windu', 'raza': 'Humano','planeta_origen':'Haruun Kal', 'color_espada': 'Morado'},
    {'nombre': 'Kli el Viejo', 'raza': 'Desconocido','planeta_origen':'Desconocido', 'color_espada': 'Desconocido'},
    {'nombre': 'Adi Gallia', 'raza': 'Tholothian','planeta_origen':'Coruscant', 'color_espada': 'Azul'},
]