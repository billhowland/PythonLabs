// cigar_party.js

let cigar_party = cigars, weekend => {
  if (weekend) {
    return (cigars >= 40);
  } else {
    return (40 <= cigars && cigars <= 60);
  }
}

let cigar_party = cigars, weekend => (cigars >= 40 && (weekend || cigars >= 60))
