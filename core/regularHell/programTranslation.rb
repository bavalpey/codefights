=begin
Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
As an avid user of CodeSignal, you find it frustrating that there are no debugging and recovery tasks in your favorite
language, PHP. You decide to help the platform by translating solutions in JavaScript into PHP.

You quickly discover that this approach is quite convenient: sometimes all you have to do is substitute the function arguments
by adding the $ sign in front of them. At first you do this manually, but soon realize that it won't get you far enough.

Now you need to implement a function that, given a solution written in JavaScript and its args, adds a $ sign in front of each
args[i] (unless there is already a dollar sign present).

Given a solution in JavaScript and its args, return the almost-PHP solution.
=end

def programTranslation(solution, args)
    argumentVariants = args.join('|')
    pattern = /(?<!\$)\b(#{argumentVariants})\b/
    repl = "$\\1"
    return solution.gsub(pattern, repl)
end
