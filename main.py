import pygame
import math

ans = 'Y'
while ans == 'Y' or ans == 'y' or ans == 'yes':
    pygame.init()


    def add_x(x, y):
        gameDisplay.blit(Ximg, (x, y))


    def add_o(x, y):
        gameDisplay.blit(Oimg, (x, y))


    def add_golire(x, y):
        gameDisplay.blit(golire, (x + 10, y + 10))


    def maxPoints(scor_P1, scor_P2, maxP):
        if scor_P1 == maxP or scor_P2 == maxP:
            return True
        else:
            return False


    def full(matrice, n, m):
        count = 0
        for i in range(0, n):
            for j in range(0, m):
                if matrice[i][j] != 0:
                    count += 1
        if count == n * m:
            return True
        else:
            return False


    def minimax(matriceNumere, adamcime, isMaximazing, scor_bot, scor_player, maxP, full):
        if scor_bot - scor_player > 0:
            return 1000
        elif scor_bot - scor_player < 0:
            return -1000
        elif scor_bot - scor_player == 0 or full:
            return 0
        if isMaximazing:
            bestScore = -1000
            for i in range(0, N):
                for j in range(0, M):
                    if matriceNumere[i][j] == 0:
                        matriceNumere[i][j] = 1
                        score = minimax(matriceNumere, 0, False, scor_bot, scor_player, maxP, full)
                        matriceNumere[i][j] = 0
                        if score > bestScore:
                            bestScore = score
            return bestScore
        else:
            if isMaximazing:
                bestScore = 1000
                for i in range(0, N):
                    for j in range(0, M):
                        if matriceNumere[i][j] == 0:
                            matriceNumere[i][j] = 2
                            score = minimax(matriceNumere, 0, True, scor_bot, scor_player, maxP, full)
                            matriceNumere[i][j] = 0
                            if score < bestScore:
                                bestScore = score
                return bestScore


    def compareMove(matriceNumere, N, M, scor_P1, scor_P2, maxP, filled):
        bestScore = -1000
        bestMovei = 0
        bestMovej = 0
        for i in range(0, N):
            for j in range(0, M):
                if matriceNumere[i][j] == 0:
                    matriceNumere[i][j] = 1
                    score = minimax(matriceNumere, 0, False, scor_P1, scor_P2, maxP, filled)
                    matriceNumere[i][j] = 0
                    if score > bestScore:
                        bestScore = score
                        bestMovei = i
                        bestMovej = j
        add_x(bestMovei * 100, bestMovej * 100)

        # return bestMove


    def calcul(matriceaValori, coloana, linia, N, M, playerSign, scor_P):
        nearPlacement = [[(linia, coloana), (linia, coloana)], [(linia, coloana), (linia, coloana)],
                         [(linia, coloana), (linia, coloana)], [(linia, coloana), (linia, coloana)]]
        temp_linie = linia
        temp_coloana = coloana
        moved = 0
        semn = int(playerSign)

        # verificare verticala in sus
        while temp_coloana > 0 and moved < 4:
            if matriceaValori[temp_linie][temp_coloana - 1] == semn:
                nearPlacement[1][0] = (temp_linie, temp_coloana - 1)
                temp_coloana -= 1
                moved += 1
            else:
                break
        temp_coloana = coloana
        temp_linie = linia
        moved = 0
        # verificare verticala in jos
        while temp_coloana < M - 1 and moved < 4:
            if matriceaValori[temp_linie][temp_coloana + 1] == semn:
                nearPlacement[1][1] = (temp_linie, temp_coloana + 1)
                temp_coloana += 1
                moved += 1
            else:
                break
        moved = 0
        temp_linie = linia
        temp_coloana = coloana
        scorVertical = 0
        if nearPlacement[1][0] != (linia, coloana) or nearPlacement[1][1] != (linia, coloana):
            if int(nearPlacement[1][1][1] - nearPlacement[1][0][1] + 1) > 4:
                scorVertical = int(int(nearPlacement[1][1][1] - nearPlacement[1][0][1] + 1) / 4) + (
                        nearPlacement[1][1][1] - nearPlacement[1][0][1] + 1) % 4
            else:
                scorVertical = int(int(nearPlacement[1][1][1] - nearPlacement[1][0][1] + 1) / 4)
        temp_linie = linia
        temp_coloana = coloana

        # verificare orizontala in stanga
        while temp_linie > 0 and moved < 4:
            if matriceaValori[temp_linie - 1][temp_coloana] == semn:
                nearPlacement[0][0] = (temp_linie - 1, temp_coloana)
                temp_linie -= 1
                moved += 1
            else:
                break
        temp_linie = linia
        temp_coloana = coloana
        moved = 0
        # verificare orizontala in dreapta
        while temp_linie < N - 1 and moved < 4:
            if matriceaValori[temp_linie + 1][temp_coloana] == semn:
                nearPlacement[0][1] = (temp_linie + 1, temp_coloana)
                temp_linie += 1
                moved += 1
            else:
                break

        temp_linie = linia
        temp_coloana = coloana
        moved = 0
        scorOrizontal = 0
        if nearPlacement[0][0] != (linia, coloana) or nearPlacement[0][1] != (linia, coloana):
            if int(nearPlacement[0][1][0] - nearPlacement[0][0][0] + 1) > 4:
                scorOrizontal = int((nearPlacement[0][1][0] - nearPlacement[0][0][0] + 1) / 4) + (
                        nearPlacement[0][1][0] - nearPlacement[0][0][0] + 1) % 4
            else:
                scorOrizontal = int((nearPlacement[0][1][0] - nearPlacement[0][0][0] + 1) / 4)

        temp_linie = linia
        temp_coloana = coloana
        moved = 0
        ###diagonala principala sus si jos
        while temp_linie > 0 and temp_coloana > 0 and moved < 4:
            if matriceaValori[temp_linie - 1][temp_coloana - 1] == semn:
                nearPlacement[2][0] = (temp_linie - 1, temp_coloana - 1)
                temp_linie -= 1
                temp_coloana -= 1
                moved += 1
            else:
                break
        temp_linie = linia
        temp_coloana = coloana
        moved = 0
        while temp_linie < N - 1 and temp_coloana < M - 1 and moved < 4:
            if matriceaValori[temp_linie + 1][temp_coloana + 1] == semn:
                nearPlacement[2][1] = (temp_linie + 1, temp_coloana + 1)
                temp_linie += 1
                temp_coloana += 1
                moved += 1
            else:
                break

        ##Diagonala secundara

        temp_linie = linia
        temp_coloana = coloana
        moved = 0

        while temp_linie > 0 and temp_coloana < M - 1 and moved < 4:
            if matriceaValori[temp_linie - 1][temp_coloana + 1] == semn:
                nearPlacement[3][0] = (temp_linie - 1, temp_coloana + 1)
                temp_linie -= 1
                temp_coloana += 1
                moved += 1
            else:
                break
        temp_linie = linia
        temp_coloana = coloana
        moved = 0
        while temp_linie < N - 1 and temp_coloana > 0 and moved < 4:
            if matriceaValori[temp_linie + 1][temp_coloana - 1] == semn:
                nearPlacement[3][1] = (temp_linie + 1, temp_coloana - 1)
                temp_coloana -= 1
                temp_linie += 1
                moved += 1
            else:
                break

        # calcul scoruri pe directii
        scorDiagonalaS = 0

        if nearPlacement[3][0] != (linia, coloana) or nearPlacement[3][1] != (linia, coloana):
            if int(nearPlacement[3][1][0] - nearPlacement[3][0][0] + 1) > 4:
                scorDiagonalaS = int((nearPlacement[3][1][0] - nearPlacement[3][0][0] + 1) / 4) + (
                        nearPlacement[3][1][0] - nearPlacement[3][0][0] + 1) % 4
            else:
                scorDiagonalaS = int((nearPlacement[3][1][0] - nearPlacement[3][0][0] + 1) / 4)
        if scorDiagonalaS > 0:
            i1 = nearPlacement[3][0][0]
            j1 = nearPlacement[3][0][1]
            i2 = nearPlacement[3][1][0]
            j2 = nearPlacement[3][1][1]
            while i1 <= i2 and j1 >= j2:
                matriceaValori[i1][j1] = 0
                add_golire(i1 * 100, j1 * 100)
                i1 += 1
                j1 -= 1

        scorDiagonalaP = 0
        if nearPlacement[2][0] != (linia, coloana) or nearPlacement[2][1] != (linia, coloana):
            if int(nearPlacement[2][1][0] - nearPlacement[2][0][0] + 1) > 4:
                scorDiagonalaP = int((nearPlacement[2][1][0] - nearPlacement[2][0][0] + 1) / 4) + (
                        nearPlacement[2][1][0] - nearPlacement[2][0][0] + 1) % 4
            else:
                scorDiagonalaP = int((nearPlacement[2][1][0] - nearPlacement[2][0][0] + 1) / 4)

        if scorDiagonalaP > 0:
            i_mic = nearPlacement[2][0][0]
            i_mare = nearPlacement[2][1][0]
            j_mic = nearPlacement[2][0][1]
            j_mare = nearPlacement[2][1][1]
            while i_mic <= i_mare and j_mic <= j_mare:
                matriceaValori[i_mic][j_mic] = 0
                add_golire(i_mic * 100, j_mic * 100)
                i_mic += 1
                j_mic += 1

        if scorOrizontal > 0:
            for i in range(nearPlacement[0][0][0], nearPlacement[0][1][0] + 1):
                matriceaValori[i][nearPlacement[0][0][1]] = 0
                add_golire(i * 100, nearPlacement[0][0][1] * 100)

        if scorVertical > 0:
            for i in range(nearPlacement[1][0][1], nearPlacement[1][1][1] + 1):
                matriceaValori[nearPlacement[1][0][0]][i] = 0
                add_golire(nearPlacement[1][0][0] * 100, i * 100)

        if scorOrizontal + scorVertical + scorDiagonalaP + scorDiagonalaS > 0:

            scor_P = scor_P + scorVertical + scorOrizontal + scorDiagonalaP + scorDiagonalaS
            if semn == 1:
                print("Scor X :", scor_P)
            if semn == 2:
                print("Scor 0 :", scor_P)
        return scor_P


    N = int(input("Introdu N "))
    M = int(input("Introdu M "))
    maxP = int(input("Numarul maxima de puncte pentru incheierea jocului "))
    if 10 >= N >= 5 and 10 >= M >= 5:
        scor_P1 = 0
        scor_P2 = 0
        dim_celula = 100
        black = (0, 0, 0)
        white = (255, 255, 255)
        red = (255, 0, 0)
        blue = (0, 0, 255)

        display_width = N * 100
        display_height = M * 100

        Ximg = pygame.image.load('x.png')
        Oimg = pygame.image.load('0.png')
        golire = pygame.image.load("patratalb.png")
        golire = pygame.transform.scale(golire, (80, 80))

        gameDisplay = pygame.display.set_mode((N * 100 + 200, M * 100))

        pygame.display.set_caption('tic tac toe + 4 in a row')

        clock = pygame.time.Clock()


        def drawGrid():
            for x in range(0, int(display_width / 100) * 100, dim_celula):
                for y in range(0, int(display_height / 100) * 100, dim_celula):
                    rect = pygame.Rect(x, y, dim_celula, dim_celula)
                    pygame.draw.rect(gameDisplay, black, rect, 1)


        filled = False
        pointsend = False

        turn = 0

        gameDisplay.fill(white)
        drawGrid()

        matriceNumere = []

        matriceCelule = []

        for linie in range(N):
            celule_temp = []
            numere = []
            for coloane in range(M):
                patr = pygame.Rect(coloane * (dim_celula + 1), linie * (dim_celula + 1), dim_celula, dim_celula)
                numere.append(0)
                celule_temp.append(patr)
            matriceNumere.append(numere)
            matriceCelule.append(celule_temp)

        schimbare0 = 0
        schimbareX = 0

        if __name__ == "__main__":

            while not filled and not pointsend:

                for event in pygame.event.get():

                    if event.type == pygame.QUIT:
                        filled = True

                    if event.type == pygame.MOUSEBUTTONUP:
                        # if turn == 0:
                        #     x, y = pygame.mouse.get_pos()
                        #     for i in range(0, display_width, 100):
                        #         for j in range(0, display_height, 100):
                        #             if i < x < i + 100 and j < y < j + 100 and matriceNumere[int(i / 100)][
                        #                 int(j / 100)] == 0:
                        #                 # add_x(i, j)
                        #                 lin = int(i / 100)
                        #                 col = int(j / 100)
                        #                 turn = turn + 1
                        #                 matriceNumere[lin][col] = 1
                        #                 scor_P1 = calcul(matriceNumere, col, lin, N, M, 1, scor_P1)
                        #                 filled = full(matriceNumere, N, M)
                        #                 pointsend = maxPoints(scor_P1, scor_P2, maxP)
                        #                 minimax(matriceNumere,0,False,scor_P1,scor_P2,maxP,filled)
                        if turn == 1:
                            x, y = pygame.mouse.get_pos()
                            for i in range(0, display_width, 100):
                                for j in range(0, display_height, 100):
                                    # if i < x < i + 100 and j < y < j + 100 and matriceNumere[int(i / 100)][
                                    #     int(j / 100)] == 2 and schimbare0 == 0:
                                    #     print("schimbare semn posibila")
                                    #     while True:
                                    #         if event.type == pygame.MOUSEBUTTONUP:
                                    #             p, o = pygame.mouse.get_pos()
                                    #             for q in range(i - 100, i + 200, 100):
                                    #                 for z in range(j - 100, i + 200, 100):
                                    #                     if q > display_width or z > display_height:
                                    #                         break
                                    #                     else:
                                    #                         if q < p < q + 100 and z < o < z + 100 and \
                                    #                                 matriceNumere[int(q / 100)][
                                    #                                     int(z / 100)] == 1 and schimbare0 == 0:
                                    #                             print("am apasat pe un simbol opus")
                                    #                             schimbare0 += 1
                                    #                             turn -= 1

                                    if i < x < i + 100 and j < y < j + 100 and matriceNumere[int(i / 100)][
                                        int(j / 100)] == 0:
                                        add_o(i, j)
                                        lin = int(i / 100)
                                        col = int(j / 100)
                                        turn = turn - 1
                                        matriceNumere[lin][col] = 2
                                        scor_P2 = calcul(matriceNumere, col, lin, N, M, 2, scor_P2)
                                        filled = full(matriceNumere, N, M)
                                        pointsend = maxPoints(scor_P1, scor_P2, maxP)
                                        schimbare0 = 0
                    if turn == 0:
                        x, y = pygame.mouse.get_pos()
                        for i in range(0, display_width, 100):
                            for j in range(0, display_height, 100):
                                if i < x < i + 100 and j < y < j + 100 and matriceNumere[int(i / 100)][
                                    int(j / 100)] == 0:
                                    # add_x(i, j)
                                    lin = int(i / 100)
                                    col = int(j / 100)
                                    turn = turn + 1
                                    matriceNumere[lin][col] = 1
                                    scor_P1 = calcul(matriceNumere, col, lin, N, M, 1, scor_P1)
                                    filled = full(matriceNumere, N, M)
                                    pointsend = maxPoints(scor_P1, scor_P2, maxP)
                                    compareMove(matriceNumere,N,M, scor_P1, scor_P2, maxP, filled)
                                    # minimax(matriceNumere, 0, False, scor_P1, scor_P2, maxP, filled)
                                    for t in range(0, N):
                                        for r in range(0, M):
                                            if matriceNumere[t][r] == 1:
                                                add_x(t * 100, r * 100)

                pygame.display.update()

                clock.tick(60)
            print("Jucatorul 0 a obtinut", scor_P2)
            print("Jucatorul X a obtinut", scor_P1)
            pygame.quit()
            quit()
    elif (N > 10 or N < 5) and (M > 10 or M < 5):
        print("N si M trebuie sa fie intre 5 si 10")
        print("Doriti sa inchideti programul")
        ans = input("Y/N\n")
    elif N > 10 or N < 5:
        print("N trebuie sa fie intre 5 si 10")
        print("Doriti sa inchideti programul")
        ans = input("Y/N\n")
    elif M > 10 or M < 5:
        print("M trebuie sa fie intre 5 si 10")
        print("Doriti sa inchideti programul")
        ans = input("Y/N\n")

pygame.quit()
quit()
