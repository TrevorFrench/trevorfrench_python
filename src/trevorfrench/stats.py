def one_way_anova(*args):
    total_length = 0
    total_sum = 0
    SSE = 0
    SSR = 0
    k = 0
    # [Xj, n]
    groups = []
    anova_table = {}

    for group in args:
        k += 1
        n = len(group)
        group_sum = sum(group)
        total_length += n
        total_sum += group_sum
        Xj = group_sum / n
        groups.append([Xj, n])
        for obs in group:
            SSE += (obs - Xj) * (obs - Xj)

    X = total_sum / total_length

    for Xj, n in groups:
        SSR += n * ((Xj - X) * (Xj - X))

    SST = SSR + SSE
    df_treatment = k - 1
    df_error = total_length - k
    df_total = total_length - 1
    MST = SSR / df_treatment
    MSE = SSE / df_error
    F = MST / MSE
 
    anova_table.update({"SST": SST
        , "SSE": SSE
        , "SSR": SSR
        , "df_treatment": df_treatment
        , "df_error": df_error
        , "df_total": df_total
        , "MST": MST
        , "MSE": MSE
        , "F": F})

    return anova_table