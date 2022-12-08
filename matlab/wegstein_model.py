def wegstein_model(x: list) -> tuple:
  nc8h8r, nc8h10r = x[0], x[1]

  nc8h10a = 100
  # nh2oa = 3000
  nc8h8ri = nc8h8r
  nc8h10ri = nc8h10a + nc8h10r
  # nh2ori = nh2oa
  r = 0.65 * nc8h10ri
  nc8h8ro = nc8h8ri + r
  nc8h10ro = nc8h10ri - r
  # nh2oro = nh2ori
  # nh2ro = r
  nc8h8oo = nc8h8ro
  nc8h10oo = nc8h10ro
  # nh2ow = nh2oro
  # nh2v = nh2ro
  nc8h8p = nc8h8oo * 0.99
  nc8h10p = nc8h10oo * 0.01
  nc8h8r2 = nc8h8oo - nc8h8p
  nc8h10r2 = nc8h10oo - nc8h10p

  return nc8h8r2, nc8h10r2