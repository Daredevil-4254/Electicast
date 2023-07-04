class Voting(sp.Contract):
    def _init_(self, candidates):
        self.init(
            voters={},
            candidates=candidates,
            votes={},
            winner=""
        )

    @sp.entry_point
    def vote(self, params):
        sp.verify(~self.data.voters.contains(sp.sender), message="You have already voted.")
        sp.verify(params.candidate in self.data.candidates, message="Invalid candidate.")

        self.data.voters[sp.sender] = True
        if params.candidate in self.data.votes:
            self.data.votes[params.candidate] += 1
        else:
            self.data.votes[params.candidate] = 1

    @sp.entry_point
    def get_winner(self, params):
        sp.verify(self.data.winner == "", message="Winner has already been determined.")

        max_votes = 0
        for candidate, votes in self.data.votes.items():
            if votes > max_votes:
                self.data.winner = candidate
                max_votes = votes

    def get_votes(self):
        return self.data.votes

@sp.add_test(name="Voting")
def test_voting():
    candidates = ["Candidate A", "Candidate B"]
    contract = Voting(candidates)

    scenario = sp.test_scenario()
    scenario.h1("Voting Contract")

    # Deploy the contract
    scenario.h2("Deploy contract")
    scenario += contract

    # Cast votes
    scenario.h2("Cast votes")
    scenario += contract.vote(candidate=candidates[0]).run(sender=sp.address("tz1Voter1"))
    scenario += contract.vote(candidate=candidates[0]).run(sender=sp.address("tz1Voter2"))
    scenario += contract.vote(candidate=candidates[1]).run(sender=sp.address("tz1Voter3"))

    # Get votes
    scenario.h2("Get votes")
    scenario += contract.get_votes().run()

    # Determine winner
    scenario.h2("Determine winner")
    scenario += contract.get_winner().run()

    # Get votes after determining winner
    scenario.h2("Get votes after determining winner")
    scenario += contract.get_votes().run()

# Entry point
if _name_ == "_main_":
    test_voting()
