# -*- coding: utf-8 -*-
import api.azlyricsPython


def main():
	artist = input("Insert list of artists (separated by '*'): ")
	api.azlyricsPython.getAndProcessArtistsPage(artist)


if __name__ == '__main__':
	main()

