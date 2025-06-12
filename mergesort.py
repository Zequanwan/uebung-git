def merge_sort(arr):  # 2 Parameternamen optimieren 7 Funktionsbenennungsformat optimieren
    """
    Sorts a list in ascending order using the merge sort algorithm.

    Args:
        arr (list): The list to be sorted.

    Returns:
        None: The input list is sorted in-place.
    """
    if (len(arr) > 1):  # 4 Optimieren von if-Funktionen
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        l = r = i = 0  # 5 Optimierung der Parametrierung

        while l < len(left) and r < len(right):
            if left[l] <= right[r]:
                arr[i] = left[l]  # 1 Direkte Zuweisung ersetzt ASSIGNMENT-Aufruf
                l += 1
            else:
                arr[i] = right[r]
                r += 1
            i += 1

        while l < len(left):
            arr[i] = left[l]
            l += 1
            i += 1

        while r < len(right):
            arr[i] = right[r]
            r += 1
            i += 1


import matplotlib.pyplot as plt

if __name__ == "__main__":  # 6 Fügen Sie den Haupteingang hinzu
    """
    Main execution block when the script is run directly.
    """
    my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    arr = my_list.copy()  # 3 Sortieren Sie die Kopie und lassen Sie die Originalliste unverändert

    # —— Plotting optimizations ——

    plt.style.use("ggplot")                              # 8 Stil aus Vorlesungsstandards setzen
    fig, axes = plt.subplots(1, 2, figsize=(12, 5), sharey=True)
                                                         # 9 Nebeneinander-Layout, gemeinsame Y-Achse

    # 10 Balkendiagramm vor dem Sortieren statt einfacher Linie
    axes[0].bar(range(len(my_list)), my_list, edgecolor="black")
    axes[0].set_title("Before Merge Sort")               # 11 Klarer, beschrifteter Titel
    axes[0].set_xlabel("Index")                          # 12 Achsenbeschriftung gemäß Standard
    axes[0].set_ylabel("Value")

    merge_sort(arr)                                      # 13 Sortierfunktion auf gerenderte Kopie anwenden

    # 14 Balkendiagramm nach dem Sortieren in passender Farbe
    axes[1].bar(range(len(arr)), arr, edgecolor="black")
    axes[1].set_title("After Merge Sort")
    axes[1].set_xlabel("Index")

    fig.suptitle("Merge Sort Visualization")             # 15 Übergeordnetes Diagrammtitel hinzufügen
    fig.tight_layout(rect=[0, 0.03, 1, 0.95])            # 16 Layout anpassen, damit nix überlappt

    plt.show()
