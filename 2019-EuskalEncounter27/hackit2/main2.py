
green = open('hackit2/green', 'rb').read()
red = open('hackit2/red', 'rb').read()
yellow = open('hackit2/yellow', 'rb').read()

size = len(red)
xord_byte_array = bytearray(size)
 
# XOR between the files
for i in range(len(yellow)):
	red[i] & yellow[i] & 255
	xord_byte_array[i] = red[i] & green[i]


open('output.txt', 'wb').write(xord_byte_array)



"""
								Ktablered1000red1000.
CREATE TABLE red1000(redz blob) ytablered100red100.
CREATE TABLE red100(reda varchar(10),redb varchar(10)) utablered9red9.
CREATE TABLE red9(reda varchar(10),redb varchar(10)) utablered8red8.
CREATE TABLE red8(reda varchar(10),redb varchar(10)) utablered7red7.
CREATE TABLE red7(reda varchar(10),redb varchar(10)) utablered6red6.
CREATE TABLE red6(reda varchar(10),redb varchar(10)) utablered5red5.
CREATE TABLE red5(reda varchar(10),redb varchar(10)) utablered4red4.
CREATE TABLE red4(reda varchar(10),redb varchar(10)) utablered3red3.
CREATE TABLE red3(reda varchar(10),redb varchar(10)) utablered2red2.
CREATE TABLE red2(reda varchar(10),redb varchar(10)) utablered1red1.
CREATE TABLE red1(reda varchar(10),redb varchar(10))

Ktablered1000red1000.
CREATE TABLE red1000(redz blob)N......ytablered100red100.
CREATE TABLE red100(reda varchar(10),redb varchar(10))H......utablered9red9.
CREATE TABLE red9(reda varchar(10),redb varchar(10))H......utablered8red8.
CREATE TABLE red8(reda varchar(10),redb varchar(10))H......utablered7red7.
CREATE TABLE red7(reda varchar(10),redb varchar(10))H......utablered6red6.
CREATE TABLE red6(reda varchar(10),redb varchar(10))H......utablered5red5.
CREATE TABLE red5(reda varchar(10),redb varchar(10))H......utablered4red4.
CREATE TABLE red4(reda varchar(10),redb varchar(10))H......utablered3red3.
CREATE TABLE red3(reda varchar(10),redb varchar(10))H......utablered2red2.
CREATE TABLE red2(reda varchar(10),redb varchar(10))H......utablered1red1.
CREATE TABLE red1(reda varchar(10),redb varchar(10))


