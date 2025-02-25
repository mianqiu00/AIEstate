def update_dataframe_with_conflict_resolution(df, new_columns, args):
    new_columns.columns = args
    
    def conflict_operation(arg1, arg2):
        if -1 in [arg1, arg2]:
            return max(arg1, arg2)
        else:
            if not arg1 == arg2:
                arg1, arg2 = int(arg1), int(arg2)
                assert arg1 == arg2
            return arg1

    for col in new_columns.columns:
        if col in df.columns:
            df[col] = df[col].combine(new_columns[col], conflict_operation)
        else:
            df[col] = new_columns[col]
    return df