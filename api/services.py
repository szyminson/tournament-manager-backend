from api.models import Duel, Participant, Tree

class TreeGenerator:
    complements = []
    arr = [1, 2]
    participants = []
    category = None
    tournament = None

    def __init__(self, category, tournament):
        self.category = category
        self.tournament = tournament
        self.participants = Participant.objects.filter(category = category)

    def divide(self, arr, depth, m):
        if len(self.complements) <= depth:
            self.complements.append(2 ** (depth + 2) + 1)
        complement = self.complements[depth]
        for i in range(2):
            if complement - arr[i] <= m:
                arr[i] = [arr[i], complement - arr[i]]
                self.divide(arr[i], depth + 1, m)
    
    def generate(self):
        participant_number = len(self.participants)
        self.divide(self.arr, 0, participant_number)
        participant_tree = self.indexes_to_participants(self.arr)
        return self.persist(participant_tree)

    def indexes_to_participants(self, arr):
        participant_tree = []
        for element in arr:
            if type(element) is list:
                participant_tree.append(self.indexes_to_participants(element))
            else:
                participant_tree.append(self.participants[element - 1])

        return participant_tree

    def create_duels(self, participant_tree, parent_duel):
        duel = Duel()
        duel.save()
        if parent_duel is not None:
            duel.parent_duel = parent_duel

        for index, element in enumerate(participant_tree):
            if type(element) is list:
                self.create_duels(element, duel)
            else:
                if index == 0:
                    duel.participant_one = element
                else:
                    duel.participant_two = element
        duel.save()
        return duel

    def persist(self, participant_tree):
        root_duel = self.create_duels(participant_tree, None)
        tree = Tree(category= self.category, tournament=self.tournament, root_duel=root_duel)
        tree.save()
        return tree
