
% =========================================================
% FAMILY TREE PROGRAM IN PROLOG
% =========================================================

% -------------------------
% Gender Facts
% -------------------------

male(john).
male(michael).
male(david).
male(james).
male(chris).

female(mary).
female(susan).
female(linda).
female(sarah).
female(emily).

% -------------------------
% Parent Relationships
% -------------------------

parent(john, michael).
parent(mary, michael).

parent(john, susan).
parent(mary, susan).

parent(michael, david).
parent(linda, david).

parent(michael, sarah).
parent(linda, sarah).

parent(susan, james).
parent(chris, james).

parent(susan, emily).
parent(chris, emily).

% -------------------------
% Rules
% -------------------------

father(X, Y) :-
    parent(X, Y),
    male(X).

mother(X, Y) :-
    parent(X, Y),
    female(X).

grandparent(X, Y) :-
    parent(X, Z),
    parent(Z, Y).

grandchild(X, Y) :-
    grandparent(Y, X).

sibling(X, Y) :-
    parent(Z, X),
    parent(Z, Y),
    X \= Y.

cousin(X, Y) :-
    parent(A, X),
    parent(B, Y),
    sibling(A, B).

uncle(X, Y) :-
    sibling(X, Z),
    parent(Z, Y),
    male(X).

aunt(X, Y) :-
    sibling(X, Z),
    parent(Z, Y),
    female(X).
