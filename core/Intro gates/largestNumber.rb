def largestNumber(n)
    this = ""
        while(n != 0)
            this += "9"
            n -= 1
        end
        return this.to_i()
end
