#include <stdio.h>
#include <time.h>
#include <stdlib.h>

int Conclusion(int WEAPON1, int WEAPON2);
int randint(int n);

int main()
{
    //WELCOME TEXT

    printf(
        "███████████████████████████████████████████████████████████████\n"
        "██▄─▄▄▀█─▄▄─█─▄▄▄─█▄─█─▄████████▄─▄▄─██▀▄─██▄─▄▄─█▄─▄▄─█▄─▄▄▀██\n"
        "███─▄─▄█─██─█─███▀██─▄▀██████████─▄▄▄██─▀─███─▄▄▄██─▄█▀██─▄─▄██\n"
        "██▄▄█▄▄█▄▄▄▄█▄▄▄▄▄█▄▄█▄▄████████▄▄▄███▄▄█▄▄█▄▄▄███▄▄▄▄▄█▄▄█▄▄██\n"
        "██████████████─▄▄▄▄█─▄▄▄─█▄─▄█─▄▄▄▄█─▄▄▄▄█─▄▄─█▄─▄▄▀███████████\n"
        "██████████████▄▄▄▄─█─███▀██─██▄▄▄▄─█▄▄▄▄─█─██─██─▄─▄███████████\n"
        "██████████████▄▄▄▄▄█▄▄▄▄▄█▄▄▄█▄▄▄▄▄█▄▄▄▄▄█▄▄▄▄█▄▄█▄▄███████████\n"
        "                                                   written in c\n"
        "                                                      by hitesh\n");

    // Variables
    int win_score = 3;
    int player_score = 0;
    int cpu_score = 0;
    int weapon1, weapon2;
    int results;

    char weapon_list[][7] = {{"Rock"}, {"Paper"}, {"Scissor"}};

    char *player1;
    player1 = (char *)malloc(5 * sizeof(char));

    // Taking player 1 input
    printf("note:- don't use space\n");
    printf("Enter your name: ");
    scanf("%s", player1);

    printf("The game is starting for %s...\n\n", player1);
    printf("Winning score: %d\n‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾\n", win_score);

    // Starting loop

    int game_start = 0;
    int game_end = 3;
    while (game_start < game_end)
    {
        game_start++;

        // If game draws this gives another chance
        if (game_start == 2)
        {
            if (player_score == cpu_score)
            {
                printf("The game is draw, hence one more turn is played.\n");
                game_start = game_start - 1;
            }
        }

        // Displaying scores
        printf("\n%s's score: %d\n", player1, player_score);
        printf("CPU's score: %d\n", cpu_score);
        printf("\n%s' Turn ==>\n\n", player1);

        // weapon selection by player1
        printf("Enter 1 for Rock, 2 for Scissors & 3 for Paper\n");
        printf("> ");
        scanf("%d", &weapon1);
        weapon1 = weapon1 - 1;
        printf("\n%s chose %s\n", player1, weapon_list[weapon1]);

        // weapon selection by cpu
        weapon2 = randint(3);
        printf("CPU chose %s\n\n", weapon_list[weapon2]);

        // Calculating Conclusion
        results = Conclusion(weapon1, weapon2);

        if (results == 1)
        {
            printf("\tDraw\n");
            printf("🏅 %s got 1 point\n", player1);
            printf("🏅 CPU got 1 point\n");
            player_score = player_score + 1;
            cpu_score = cpu_score + 1;
        }
        else if (results == 2)
        {
            printf("🏅 %s got 1 point\n", player1);
            player_score = player_score + 1;
        }
        else if (results == 3)
        {
            printf("🏅 CPU got 1 point\n");
            cpu_score = cpu_score + 1;
        }
    }

    if (player_score > cpu_score)
    {
        printf("\n%s's score: %d\n", player1, player_score);
        printf("CPU's score: %d\n", cpu_score);
        printf("\n🏆 %s is Winner🎉\n", player1);
    }
    else if (player_score < cpu_score)
    {
        printf("\n%s's score: %d\n", player1, player_score);
        printf("CPU's score: %d\n", cpu_score);
        printf("\n🏆 CPU is Winner🎉\n", player1);
    }

    free(player1);

    return 0;
}


int randint(int n)
{
    srand(time(NULL)); // srand takes seed as an input and defined inside stdlib.h
    return rand() % n;
}



int Conclusion(int WEAPON1, int WEAPON2)
{
    int result;
    // for weapon => 0 = rock, 1 = scissors & 2 = paper
    // for result => 1 for draw, 2 = win & 3 = lost

    if (WEAPON1 == 0)
    {
        if (WEAPON2 == 0)
        {
            result = 1;
        }
        else if (WEAPON2 == 1)
        {
            result = 2;
        }
        else if (WEAPON2 == 2)
        {
            result = 3;
        }
    }

    else if (WEAPON1 == 1)
    {
        if (WEAPON2 == 0)
        {
            result = 1;
        }
        else if (WEAPON2 == 1)
        {
            result = 2;
        }
        else if (WEAPON2 == 2)
        {
            result = 3;
        }
    }

    else if (WEAPON1 == 2)
    {
        if (WEAPON2 == 0)
        {
            result = 1;
        }
        else if (WEAPON2 == 1)
        {
            result = 2;
        }
        else if (WEAPON2 == 2)
        {
            result = 3;
        }
    }

    return result;
}
