data = {
    'id': '50654ddff44f800200000004', 
    'name': 'Multiply', 
    'slug': 'multiply', 
    'category': 'bug_fixes', 
    'publishedAt': '2013-05-18T18:40:17.975Z', 
    'approvedAt': '2013-12-03T15:41:04.738Z', 
    'languages': ['javascript', 'coffeescript', 'ruby', 'python', 'haskell', 'clojure', 'java', 'csharp', 'elixir', 'cpp', 'typescript', 'php', 'crystal', 'dart', 'rust', 'fsharp', 'swift', 'go', 'shell', 'c', 'lua', 'sql', 'bf', 'r', 'nim', 'erlang', 'objc', 'scala', 'kotlin', 'solidity', 'groovy', 'fortran', 'nasm', 'julia', 'powershell', 'purescript', 'elm', 'ocaml', 'reason', 'idris', 'racket', 'agda', 'coq', 'vb', 'forth', 'factor', 'prolog', 'cfml', 'lean', 'cobol', 'haxe', 'commonlisp', 'raku', 'perl', 'pascal'], 
    'url': 'https://www.codewars.com/kata/50654ddff44f800200000004', 
    'rank': {'id': -8, 'name': '8 kyu', 'color': 'white'}, 
    'createdAt': '2012-09-28T07:12:31.171Z', 
    'approvedBy': {'username': 'alchemy', 'url': 'https://www.codewars.com/users/alchemy'}, 
    'description': 'This code does not execute properly. Try to figure out why.', 
    'totalAttempts': 5113379, 
    'totalCompleted': 4149381, 
    'totalStars': 1454, 
    'voteScore': 11887, 
    'tags': ['Bugs', 'second', 'third'], 
    'contributorsWanted': True, 
    'unresolved': {'issues': 1, 'suggestions': 2}
}

kata = {}

kata['description'] = data['description']
kata['tags'] = ', '.join(data['tags'])
kata['rank'] = data['rank']['name']
kata['url'] = data['url'] + '/solutions/'
print(kata['tags'])