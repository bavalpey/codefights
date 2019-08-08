"""
You have been watching a video for some time. Knowing the total video duration find out what portion of the video you have
already watched.

Example

For part = "02:20:00" and total = "07:00:00", the output should be
  videoPart(part, total) = [1, 3].

You have watched 1 / 3 of the whole video.
"""

from fractions import Fraction as frac

def videoPart(part, total):
  part = part.split(":")
  total = total.split(":")
  
  p_seconds = int(part[0]) * 3600 + int(part[1]) * 60 + int(part[2])
  
  t_seconds = int(total[0]) * 3600 + int(total[1]) * 60 + int(total[2])
  
  j = frac(p_seconds, t_seconds)
  
  return (j.numerator, j.denominator)
